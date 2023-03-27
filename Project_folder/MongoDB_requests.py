from pymongo import MongoClient


class MongoCommons(object):
    def __init__(self):
        self.client = MongoClient(
            'mongodb+srv://qa_agency:veHt1JK5@cluster0.qnr3p.mongodb.net/trado_qa?retryWrites=true&w=majority')
        self.db = self.client['trado_qa']
        self.users = self.db['users']
        self.products = self.db['products']


class MongoRequests(MongoCommons):
    def find_login_code(self, registered_num):
        for user in self.users.find({'phone': registered_num}):
            existing_user = user
            login_code = existing_user.get('loginCode')
            return login_code

    def assert_user_exists(self, registered_num):
        for user in self.users.find({'phone': registered_num}):
            assert user

    def get_mailing_list_status(self, registered_num):
        for user in self.users.find({'phone': registered_num}):
            existing_user = user
            mailing_list = existing_user.get('marketingList')
            return mailing_list

    def get_product_count(self):
        doc_count = self.products.estimated_document_count()
        return doc_count
