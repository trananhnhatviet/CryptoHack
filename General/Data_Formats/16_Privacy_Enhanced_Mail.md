# **#Privacy-Enhanced Mail?**

-    Đề cho ta 1 file Privacy_enhanced_mail?.pem và ta phải mở file này

-    Đề đã hướng dẫn là mở với khóa riêng 'd'

-    Đoạn code sẽ như sau:
```
    from Crypto.PublicKey import RSA

    f = open('privacy_enhanced_mail.pem','r').read()
    flag = RSA.importKey(f)

    print(flag.d)

```

-    Và cờ của bài này là: ***15682700288056331364787171045819973654991149949197959929860861228180021707316851924456205543665565810892674190059831330231436970914474774562714945620519144389785158908994181951348846017432506464163564960993784254153395406799101314760033445065193429592512349952020982932218524462341002102063435489318813316464511621736943938440710470694912336237680219746204595128959161800595216366237538296447335375818871952520026993102148328897083547184286493241191505953601668858941129790966909236941127851370202421135897091086763569884760099112291072056970636380417349019579768748054760104838790424708988260443926906673795975104689***

-    Bổ sung:
        #RSAPrivateKey ::= SEQUENCE {
        #   version           Version,
        #   modulus           INTEGER,  -- n
        #   publicExponent    INTEGER,  -- e
        #   privateExponent   INTEGER,  -- d
        #   prime1            INTEGER,  -- p
        #   prime2            INTEGER,  -- q
        #   exponent1         INTEGER,  -- d mod (p-1)
        #   exponent2         INTEGER,  -- d mod (q-1)
        #   coefficient       INTEGER,  -- (inverse of q) mod p
        #   otherPrimeInfos   OtherPrimeInfos OPTIONAL
        # }                                                                        
    
    +   Như bài trên, trong file pem, thì ta thấy nó là file private, nên ta dùng khóa 'd' để giải mã