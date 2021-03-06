"""
This module provides an interface to the Elasticsearch database.
"""
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionTimeout

class ElasticsearchInterface(object):
    """
    The Elasticsearch interface manages the connection to the elasticsearch
    database.
    """
    def __init__(self, host='localhost', port=9200):
        self.host = host
        self.port = port
        self.es = Elasticsearch([":".join([str(host), str(port)])])

    def create(self, *args, **kwargs):
        """
        The create method allows for documents passed to be elasticsearch handler
        directly.
        """
        # date = kwargs.get("date", None)
        # parser = kwargs.get('parser', 'default')
        # doctype = kwargs.get('type', 'default')
        # document = kwargs.get('document', {})
        # 
        # if date:
        #     # Index document into an index based on index_date field
        #     options = {
        #         "index": "dminer-%s-%s" % (parser, date),
        #         "doc_type": doctype,
        #         "body": document
        #     }
        # else:
        #     options = {
        #         "index": "dminer-%s" % parser,
        #         "doc_type": doctype,
        #         "body": document
        #     }

        while True:
            try:
                value = self.es.index(*args, **kwargs)
            except ConnectionTimeout:
                print "Connection Timeout"
                continue
            break
        return value

    def find(self, *args, **kwargs):
        """
        Allows for the searching of documents currently in the elasticsearch
        database.
        """
        return self.es.search(*args, **kwargs)

    def delete(self, index, doctype, doc_id):
        """
        TODO: IMPLEMENT
        """
        raise NotImplementedError()

    def update(self, index, doctype, doc_id, document):
        """
        TODO: IMPLEMENT
        """
        raise NotImplementedError()
