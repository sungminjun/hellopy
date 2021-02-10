# fizzbuzz with method .. 
def fizzbuzz(start_num, end_num, conds) -> None:
    s=range(start_num, end_num)
    combinatedConds={}
    sorted(conds)

    for i in range(conds.items().len()-1):
        conds[i].key
        conds[i+1].key

    for i in s:
        flag = False
        for (k, v) in conds.items():
            if(not i%k):
                print(v)
                flag=True
        if not flag: 
            print(i); flag=False

co = {3:'fizz',5:'buzz'}
fizzbuzz(1, 20, co)

# python do not support function overloading! can't make like this: fizzbuzz(end_num, conds) { return fizzbuzz(1, end_num, conds) }

# practice iter on objects
co = {3:'fizz',5:'buzz',7:'hoge',11:'fuga'}

co.keys
co.keys()

# TODO: ake scalable? set co size 10 and get all-of-case from that fizz buzz hoge fugas
# e.g 3:'fizz',5:'buzz',7:'hoge',11:'fuga'
# 3 fizz 5 buzz 7 hoge 11 fuga
# 15 fizzbuzz 21 fizzhoge 33 fizzfuga 35 buzzhoge 55buzzfuga 77 hogefuga 
# 105 fizzbuzzhoge 165 fizzbuzzfuga 385 buzzhogefuga....

# NOTE first 10 prime numbers (except 2) 3, 5, 7, 11, 13, 17, 19, 23, 29, 31