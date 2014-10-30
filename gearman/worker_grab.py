#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
#
#   Author  :   
#   E-mail  :   
#   Date    :   2014/02/25 
#   Desc    :
#


class WorkerGrab:
    DO_GRAB = False
    connection_handler_list = []
    
    def init_connection_handler_list(self, connection_to_handler_map):
        for connection in connection_to_handler_map:
            connection_handler = {}
            connection_handler['connection'] = connection
            connection_handler['handler'] = connection_to_handler_map[connection]
            connection_handler['dummy_noop_flag'] = False

            WorkerGrab.connection_handler_list.append(connection_handler)

    def reset_connection_handler_list(self, list):
        del WorkerGrab.connection_handler_list[:]
        WorkerGrab.connection_handler_list = list[:]

    def get_dummy_noop_flag_by_connection(self, connection):
        for connection_handler in WorkerGrab.connection_handler_list:
            if connection == connection_handler['connection']:
                return connection_handler['dummy_noop_flag']
        return False

    def update_connection_handler_list(self, connection_to_handler_map):
        tmp_connection_handler_list = []
        for connection in connection_to_handler_map:
            connection_handler = {}
            connection_handler['connection'] = connection
            connection_handler['handler'] = connection_to_handler_map[connection]
            connection_handler['dummy_noop_flag'] = self.get_dummy_noop_flag_by_connection(connection)
            tmp_connection_handler_list.append(connection_handler)

        self.reset_connection_handler_list(tmp_connection_handler_list)

    def set_dummy_noop_flag_by_handler(self, handler, dummy_noop_flag=False):
        for connection_handler in WorkerGrab.connection_handler_list:
            if handler == connection_handler['handler']:
                connection_handler['dummy_noop_flag'] = dummy_noop_flag
            

    def get_dummy_noop_flag_by_handler(self, handler):
        for connection_handler in WorkerGrab.connection_handler_list:
            if handler == connection_handler['handler']:
                return connection_handler['dummy_noop_flag']
        return False


    def get_dummy_noop_handler(self, exlude_handler=None):
        for connection_handler in WorkerGrab.connection_handler_list:
            if not exlude_handler and exlude_handler == connection_handler['handler']:
                continue
            if connection_handler['dummy_noop_flag']:
                return connection_handler['handler']
        return None
        
    def set_all_dummy_noop_flag_true(self, exlude_handler=None):
        for connection_handler in WorkerGrab.connection_handler_list:
            if not exlude_handler and exlude_handler == connection_handler['handler']:
                self.set_dummy_noop_flag_by_handler(exlude_handler, False)
            else:
                self.set_dummy_noop_flag_by_handler(connection_handler['handler'], True)
