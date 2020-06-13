import random


class Responder:
    """
    応答クラス
    """

    def __init__(self, name):
        """

        :param name Respoderオブジェクトの名前:
        """
        self.name = name

    def response(self, input):
        """
        :param input 入力された文字列:
        :return 応答文字列:
        """
        return ''

    def get_name(self):
        """応答オブジェクトの名前を返す
        """
        return self.name


class RepeatResponder(Responder):
    """おうむ返しのためのサブクラス
    """

    def response(self, input):
        """応答文字列を返す
        :param input 入力された文字列
        """

        return '{}って何'.format(input)


class RandomResponder(Responder):
    """ランダムな応答を行う
    """

    def __init__(self, name):
        """

        :param name Responderオブジェクトの名前:
        """
        replyList = ['いい天気やな', '調子はどうや', 'あめちゃんあげる']

        super().__init__(name)

        self.responses = replyList

    def response(self, input):
        """
        応答文字列を返す
        :param input　入力された値:
        :return　ランダムに返す:
        """
        return (random.choice(self.responses))
