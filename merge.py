def unique_names(names1, names2):
    def uniq(names):
        m1 = []
        for i in names:
            if i not in m1:
                m1.append(i)
        return m1
    return (uniq(names1) or uniq(names2)) + list(set(names2) - set(names1))


names1 = ["Ava", "Emma", "Olivia", "Emma", "Ava"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))  # should print Ava, Emma, Olivia, Sophia
