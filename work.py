#!/usr/bin/python3
# coding=gbk
# -*- coding: utf-8 -*-
import re
import urllib.request
import urllib.parse
import time


def craw(chinese):
    url = 'http://hanyu.baidu.com/s?wd=' + urllib.parse.quote(chinese) + '&ptype=zici'

    header = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }

    serverError = True
    while serverError:
        try:
            request = urllib.request.Request(url, headers=header)
            reponse = urllib.request.urlopen(request).read()
            html = str(reponse)

            imgs = re.compile('data-gif="(.+?\.gif)"').findall(html)
            for img in imgs:
                imagename = 'D:/���ֱʻ�/' + chinese + '.gif'
                imageurl = img
                try:
                    urllib.request.urlretrieve(imageurl, filename=imagename)
                except:
                    print(chinese + ' failure')
            serverError = False
        except:
            print(chinese + 'server error')
            time.sleep(2)
strs = ['һ','��','��','ʮ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ʿ','��','��','��','��','��','��','��','��','��','��','С','��','��','ɽ','ǧ','��','��','��','��','��','��','��','��','Ϧ','��','ô','��','��','��','��','֮','ʬ','��','��','��','��','��','Ҳ','Ů','��','��','ϰ','��','��','��','��','��','��','��','��','��','��','Ԫ','ר','��','��','��','ľ','��','֧','��','��','̫','Ȯ','��','��','��','��','ƥ','��','��','��','��','��','��','��','��','ֹ','��','��','��','��','��','��','ˮ','��','��','ţ','��','ë','��','��','��','��','ʲ','Ƭ','��','��','��','��','��','��','��','צ','��','��','��','��','��','��','��','��','��','��','��','��','��','Ƿ','��','��','��','��','��','��','��','��','��','��','Ϊ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','Ȱ','˫','��','��','��','��','ʾ','ĩ','δ','��','��','��','��','��','��','��','��','ȥ','��','��','��','��','��','��','��','��','��','��','��','ʯ','��','��','ƽ','��','��','��','��','��','ռ','ҵ','��','˧','��','��','��','Ŀ','Ҷ','��','��','��','��','��','��','��','ʷ','ֻ','��','��','��','��','��','߶','̾','��','��','ʧ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','˦','ӡ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','֭','��','ͷ','��','��','Ѩ','��','��','д','��','��','ѵ','��','��','Ѷ','��','��','˾','��','��','��','��','��','ū','��','��','Ƥ','��','��','��','ʥ','��','̨','ì','��','ĸ','��','˿','ʽ','��','��','��','��','��','��','��','��','��','ִ','��','��','��','ɨ','��','��','��','��','��','â','��','֥','��','��','��','Ȩ','��','��','��','Э','��','ѹ','��','��','��','��','��','��','ҳ','��','��','��','��','��','��','��','��','��','��','а','��','��','��','��','��','��','ʦ','��','��','��','��','��','��','��','��','��','��','��','ͬ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','Ǩ','��','ΰ','��','ƹ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','α','��','Ѫ','��','��','��','��','��','ȫ','��','ɱ','��','��','��','��','ү','ɡ','��','��','��','��','Σ','Ѯ','ּ','��','��','��','��','��','ɫ','׳','��','��','ׯ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','æ','��','��','��','լ','��','��','��','��','��','��','ũ','��','��','��','Ѱ','��','Ѹ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','Ϸ','��','��','��','��','��','��','��','Լ','��','��','Ѳ','��','Ū','��','��','��','��','��','Զ','Υ','��','��','��','̳','��','��','��','��','��','��','��','ַ','��','��','��','��','��','��','��','ץ','��','��','Т','��','��','Ͷ','��','��','��','��','��','��','��','־','Ť','��','��','��','��','ȴ','��','ѿ','��','��','��','��','��','��','«','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ҽ','��','��','��','��','��','��','��','��','��','��','��','��','ʱ','��','��','��','��','��','԰','��','Χ','ѽ','��','��','��','��','��','��','��','Ա','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ͺ','��','˽','ÿ','��','��','��','��','��','��','��','��','��','Ӷ','��','��','ס','λ','��','��','��','��','��','��','��','��','��','ϣ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ɾ','��','��','��','ӭ','��','��','ϵ','��','��','״','Ķ','��','��','��','��','Ӧ','��','��','��','��','��','ұ','��','��','��','��','��','��','��','��','��','ɳ','��','��','��','��','û','��','��','��','��','��','��','��','��','��','��','��','��','��','֤','��','��','��','��','��','ʶ','��','��','��','��','��','��','��','��','��','β','��','��','��','��','��','��','½','��','��','��','��','��','��','��','Ŭ','��','��','��','��','��','ɴ','��','��','��','��','��','ֽ','��','��','¿','Ŧ','��','��','��','��','��','��','��','��','��','Ĩ','£','��','��','��','̹','Ѻ','��','��','��','��','��','��','��','ӵ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','̧','��','ȡ','��','��','ï','ƻ','��','Ӣ','��','ֱ','��','��','é','��','֦','��','��','��','��','��','ǹ','��','��','��','��','ɥ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','̬','ŷ','¢','��','��','��','ת','ն','��','��','��','��','��','��','��','Щ','��','²','��','��','��','��','��','��','ζ','��','��','��','��','��','��','��','��','��','��','��','��','��','ӽ','��','��','��','��','��','��','��','��','��','��','��','ͼ','��','��','֪','��','��','��','��','��','��','��','��','ί','��','��','��','ʹ','��','��','ֶ','��','��','ƾ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','̰','��','ƶ','��','��','֫','��','��','��','��','��','��','в','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ҹ','��','��','��','��','��','��','��','ä','��','��','��','բ','��','֣','ȯ','��','��','��','��','��','��','¯','ĭ','ǳ','��','й','��','մ','��','��','��','��','��','ע','к','Ӿ','��','��','��','��','��','��','��','��','��','��','��','ѧ','��','��','��','��','��','��','��','��','��','ʵ','��','��','ʫ','��','��','��','��','��','��','��','��','ѯ','��','��','��','��','¼','��','��','��','ˢ','��','��','��','��','��','��','��','��','��','��','��','��','ʼ','��','��','��','��','��','��','ϸ','ʻ','֯','��','פ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ͦ','��','˩','ʰ','��','ָ','��','��','��','ƴ','��','��','��','Ų','ĳ','��','��','��','��','��','��','��','��','��','ã','��','��','��','��','��','ҩ','��','��','��','��','��','��','��','��','��','��','��','��','Ҫ','��','��','��','��','ש','��','��','��','��','��','��','ˣ','ǣ','��','��','��','ѻ','��','��','ս','��','��','��','��','ʡ','��','��','��','��','գ','��','��','��','ð','ӳ','��','��','η','ſ','θ','��','��','��','Ϻ','��','˼','��','��','Ʒ','��','��','��','��','��','��','ҧ','��','��','̿','Ͽ','��','��','��','��','��','��','��','Կ','��','ж','��','��','��','��','��','��','ѡ','��','��','��','��','��','��','��','��','��','��','��','��','��','˳','��','��','��','��','��','��','��','��','��','Ȫ','��','��','׷','��','��','��','��','��','��','��','��','��','ʳ','��','��','ʤ','��','��','��','��','��','ʨ','��','��','��','��','ó','Թ','��','��','ʴ','��','��','��','��','��','��','ͤ','��','��','��','ͥ','��','��','��','��','��','��','��','��','ʩ','��','��','��','��','��','��','��','��','��','��','��','ǰ','��','��','��','��','ը','��','��','��','��','��','��','��','��','��','��','ϴ','��','��','Ǣ','Ⱦ','��','��','��','��','Ũ','��','��','��','ǡ','��','��','��','��','��','��','��','��','ͻ','��','��','��','��','��','��','��','��','��','ף','��','��','˵','��','��','��','��','��','��','��','��','ü','��','��','��','Ժ','��','��','��','��','��','ŭ','��','��','ӯ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ͳ','��','��','��','̩','��','��','��','��','��','յ','��','��','��','��','��','��','��','��','��','��','��','��','׽','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','Ī','��','��','��','��','��','��','��','��','ͩ','��','��','��','��','У','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ԭ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ɹ','��','��','Ѽ','��','��','��','��','��','��','��','��','��','��','��','��','Բ','��','��','Ǯ','ǯ','��','��','��','Ǧ','ȱ','��','��','��','��','��','��','��','��','��','��','��','��','��','͸','��','Ц','��','ծ','��','ֵ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','Ϣ','ͽ','��','��','��','��','��',';','��','��','��','��','��','��','֬','��','��','��','��','��','��','��','��','��','��','��','��','��','��','˥','��','ϯ','׼','��','��','֢','��','��','��','ƣ','Ч','��','��','��','��','վ','��','��','��','��','��','��','��','��','ƿ','ȭ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','Ϳ','ԡ','��','��','��','��','��','��','��','ӿ','��','��','��','��','��','��','��','��','��','��','խ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','˭','��','ԩ','��','̸','��','��','��','չ','��','м','��','��','��','��','��','��','��','ͨ','��','��','Ԥ','ɣ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','̽','��','��','ְ','��','��','��','��','��','��','��','��','��','��','Ƽ','��','Ӫ','е','��','��','÷','��','��','��','Ͱ','��','��','Ʊ','��','ˬ','��','Ϯ','ʢ','ѩ','��','��','��','ȸ','��','��','��','��','��','��','��','��','Ұ','��','��','��','��','Ծ','��','��','��','��','��','Ψ','��','ո','��','Ȧ','ͭ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ż','͵','��','��','ͣ','ƫ','��','��','��','��','��','б','��','��','Ϥ','��','��','��','��','��','��','��','��','��','��','��','��','è','��','��','��','��','��','��','��','��','��','��','��','ӹ','¹','��','��','��','��','��','��','��','��','��','��','ճ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','Һ','��','��','��','��','��','��','ϧ','��','��','��','��','��','��','��','��','��','��','Ҥ','��','ı','��','��','��','��','��','��','��','��','��','¡','��','��','��','��','��','��','��','��','��','ά','��','��','��','��','��','��','��','��','��','��','Խ','��','��','��','��','��','��','��','ϲ','��','��','��','��','Ԯ','��','��','§','��','��','��','˹','��','��','��','ɢ','��','��','��','��','��','��','��','��','��','��','��','��','��','ֲ','ɭ','��','��','��','��','��','��','��','��','��','��','��','��','Ӳ','ȷ','��','ֳ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ι','��','��','��','ñ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','̺','��','ʣ','��','��','ϡ','˰','��','��','��','��','ɸ','Ͳ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ѭ','ͧ','��','��','��','��','��','Ƣ','ǻ','³','��','��','Ȼ','��','װ','��','��','ʹ','ͯ','��','��','��','��','��','��','��','��','��','��','��','��','ʪ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ԣ','��','ȹ','л','ҥ','ǫ','��','��','ǿ','��','��','��','϶','��','ɩ','��','��','��','��','ƭ','Ե','��','��','��','��','��','��','��','��','��','��','Я','��','ҡ','��','��','̯','��','��','ȵ','��','Ĺ','Ļ','��','��','��','��','��','��','��','��','��','��','¥','��','��','��','��','��','��','��','��','��','µ','��','��','��','��','��','��','��','��','��','˯','��','��','��','ů','��','Ъ','��','��','��','��','��','·','��','ǲ','��','��','ɤ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','ǩ','��','��','��','��','��','ɵ','��','��','΢','��','ң','��','��','��','��','��','��','��','��','̵','��','��','��','��','��','��','��','��','��','ú','��','��','Į','Դ','��','��','��','Ϫ','��','��','��','��','̲','��','��','��','��','��','Ⱥ','��','��','��','��','��','��','��','��','��','��','��','ǽ','Ʋ','��','��','��','��','��','ժ','ˤ','��','��','Ľ','ĺ','��','ģ','��','��','ե','��','��','��','��','��','��','Ը','��','��','��','��','��','��','��','Ӭ','֩','׬','��','��','��','��','��','��','��','��','��','��','ò','Ĥ','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','Ǹ','Ϩ','��','��','Ư','��','��','��','©','��','կ','��','��','��','��','��','��','��','��','��','��','��','˺','��','Ȥ','��','��','��','ײ','��','��','��','Ь','��','��','��','��','ӣ','��','Ʈ','��','��','��','ù','��','��','��','Ϲ','Ӱ','��','̤','��','��','��','��','��','ī','��','��','��','��','��','��','��','��','ƪ','��','��','Ƨ','��','��','ϥ','��','��','Ħ','��','��','��','��','Ǳ','��','��','��','ο','��','��','��','��','н','��','��','��','��','��','��','��','��','��','��','��','Ĭ','��','��','��','��','��','��','��','ĥ','��','��','��','��','��','ȼ','��','��','��','��','��','��','��','��','��','��','˪','ϼ','��','��','��','��','��','��','Ӯ','��','��','��','��','��','��','��','��','��','��','��','ӥ','��','��','��','��','��','��','��','��','ҫ','��','��','��','��','ħ','��','��','��','¶','��','��']
for st in strs:
    craw(st)
    time.sleep(2)