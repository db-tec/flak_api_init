class Tarefa():
    def __init__(self, titulo, descricao, dt_expiracao, projeto):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__dt_expiracao = dt_expiracao
        self.__projeto = projeto

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def dt_expiracao(self):
        return self.__dt_expiracao

    @dt_expiracao.setter
    def dt_expiracao(self, dt_expiracao):
        self.__dt_expiracao = dt_expiracao

    @property
    def projeto(self):
        return self.__projeto

    @projeto.setter
    def projeto(self, projeto):
        self.__projeto = projeto