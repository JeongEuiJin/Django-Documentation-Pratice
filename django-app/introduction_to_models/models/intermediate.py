from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    @property
    def current_club(self):
        return self.current_tradinfo.club

    @property
    def current_tradinfo(self):
        return self.tradinfo_set.get(date_leaved__isnull=True)

        # current_club프로퍼티에 현재 속하는 Club리턴
        # current_tradeinfo프로퍼티에 현재 자신의 TradeInfo리턴


class Club(models.Model):
    name = models.CharField(max_length=40)
    players = models.ManyToManyField(
        Player,
        through='TradInFo',
        through_fields=('club','player'),
    )

    def __str__(self):
        return self.name

    def squad(self, year=None):
        if year:
            return self.players.filter(
                tradinfo__date_joined__lte=date(year+1,1,1),
                tradinfo__date_leaved__gt=date(year,1,1),
            )


        else:
            return self.players.filter(tradinfo__date_leaved__isnull=True)
            pass
        # squad메서드에 현직 선수들만 리턴
        # 인수로 년도(2017, 2015...등)를 받아
        # 해당 년도의 현직 선수들을 리턴,
        # 주어지지 않으면 현재를 기준으로 함


class TradInFo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_leaved = models.DateField(null=True, blank=True)
    recommender = models.ForeignKey(
        Player,
        on_delete=models.PROTECT,
        related_name='tradinfo_set_by_recommender',
        null=True,
        blank=True,
    )

    prev_club = models.ForeignKey(
        Club,
        on_delete=models.PROTECT,
        related_name='+',
        null=True,
        blank=True,
    )

    def __str__(self):

        return '{}, {} ({} ~{})'.format(
            self.player.name,
            self.club.name,
            self.date_joined,
            self.date_leaved or '현직'
            # self.date_leaved if self.date_leaved else '현직'

        )
    @property
    def is_current(self):
        return self.date_leaved is None
        # return not self.date_leaved



    # prev_club = 이전 Club

    # 1. property로 is_current 속성이 TradeInfo가 현재 현직(leaved하지 않았는지)여부 반환
    # 2. recommender와 prev_club을 활성화시키고 Club의 MTM필드에 through_fields를 명시


    # 위의 요구조건들을 만족하는 실행코드 작성
