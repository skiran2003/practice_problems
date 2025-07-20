def proper_subset(s1,s2):
    if s2.issubset(s1):
        if s1!=s2:
            print(f"{s2} is proper subset of {s1}")
        else:
            print(f"{s2} is subset of {s1}")

s1={1,4,6,9,20}
s2={4,1,6,9,20}
s3={1,20}
proper_subset(s1,s2)
proper_subset(s1,s3)

