from respoder import *


class Nekyo:
    """メインクラス"""

    def __init__(self, name):
        """
        オブジェクトの名前はnameへ
        返答はResponderオブジェクトを作り格納する。
        :param name Nekyoオブジェクトの名前:
        """
        self.name = name
        self.responder = RandomResponder('Random')

    def dialogue(self, input):
        """

        :param inputユーザによって入力された文字列:
        :return　応答文字列:
        """

        return self.responder.response(input)

    def get_responder_name(self):
        """
        応答オブジェクトの名前を返す
        :return:
        """
        return self.responder.name

    def get_name(self):
        """
        nekyoオブジェクトの名前を返す
        :return:
        """
        return self.name
