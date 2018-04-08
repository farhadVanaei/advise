from sqlalchemy import desc

from map import *

class crud:
    def __init__(self,model_name = None):
        self.tablename = model_name
        self.model = self.__getInstance(name=model_name)

    @property
    def TableName(self):
        return self.model

    @TableName.setter
    def TableName(self,name=""):
        if name is "":
            raise Exception("table name could not be empty")
        self.tablename = name.lower()
        self.model = self.__getInstance()

    def __getInstance(self,name=None):
        if name is not None:
            name = name.lower()
            try:
                return model_list[name]
            except KeyError,e:
                return model_list[self.tablename]
        elif self.tablename is not None:
            return model_list[self.tablename]
        else:
            raise Exception("Table Name Is Not Valid ")


    def getAllTitle(self):
        columns = []
        for x in self.model.__table__.columns:
            arr = str(x).split(".")
            columns.append(arr[1])
        return columns

    def getAllByPageNumber(self,pagenumber=1):
        result = self.model.query
        return result.order_by(desc(self.model.id)).paginate(page=pagenumber,per_page=9,error_out=False)

    def listAll(self,page=1):
        try:
            page = int(page)
        except:
            page = 1

        if page == 0 :
            page = 1
        title = self.getAllTitle()
        try:
            result = self.getAllByPageNumber(page)
        except:
            result = self.getAllByPageNumber(1)
        answer = {}
        for x in range(1, 10):
            temp_dic = {}
            for y in title:
                temp_dic[str(y)] = getattr(result.items[x-1], y)
            answer[str(x)] = temp_dic
        # print answer
        return answer