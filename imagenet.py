# -*- coding: utf-8 -*-

import urllib2
import socket
import types

def main():
    # download synsets list
    row_synset_list = urllib2.urlopen('http://www.image-net.org/api/text/imagenet.synset.obtain_synset_list', timeout=socket._GLOBAL_DEFAULT_TIMEOUT)
    synset_list = row_synset_list.read().split('\n')
#print synset_list

    for wnid in synset_list:
        url = 'http://www.image-net.org/api/text/wordnet.structure.hyponym?wnid=' + wnid + '&full=1'
        row_hyponym = urllib2.urlopen(url, timeout=socket._GLOBAL_DEFAULT_TIMEOUT)
        hyponym_list = row_hyponym.read().split('\n')
        # none hyponym
        if len(hyponym_list) == 2:
            pass
        # hyponyms
        else:
            pass
            

if __name__ == '__main__':
    main()