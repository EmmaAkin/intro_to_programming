def ransom_note(magazine, rasom):
    result = True
    magazine_words = dict()
    randsom_words = dict()
    for i in ransom:
        randsom_words[i] = randsom_words.get(i,0)+1

    for i in magazine:
        magazine_words[i] =magazine_words.get(i,0)+1

    for key, value in randsom_words.items():
        if key in magazine and (value == magazine_words[key]):continue
        else:
            result = False
            return result
    return result


# m, n = map(int, input().strip().split(' '))
# magazine = input().strip().split(' ')
# ransom = input().strip().split(' ')

magazine = "wi z ne we ebixk yvrd qrd ojckw q xe e bcco xb ieqym dwuu w dnapw achkt xqdhs nstms zmqu csqxi rim tvic arq fvjqx x su ty zl zmah y tv rkjq hpvpx ujj f i u fl iv n mnrvx tho diz k tidi gr ptkq z tho su diz yvrd dwuu dnapw xb arq xb mnrvx xe bcco qrd y ptkq rim fvjqx bcco q q wi i tidi gr mnrvx hpvpx tv f y mnrvx we fvjqx tv f wi ptkq ujj rim ebixk tho ptkq rkjq yvrd dwuu zl ujj zl qrd e ieqym".split(" ")
ransom = "dwuu tvic y dnapw ujj tidi nstms x xe achkt x su zmqu iv zmqu xb ojckw we fvjqx tvic tv ne rkjq diz tvic we rkjq nstms zmah ieqym zmah fl xb wi tho x z ty u i gr ptkq q su tho rim tv iv iv yvrd xe qrd y dnapw q zmah arq we ieqym su zl q xb arq rkjq q e xb zl ty fvjqx ptkq ieqym qrd y wi wi nstms diz dnapw zmah q ebixk su e xb q i mnrvx wi x x tidi w ojckw bcco e tv rkjq tho".split(" ")

answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")

