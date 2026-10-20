def TotalOf(Items):
    unused = 0
    Result = 0
    for Item in Items:
        Result = Result + Item
    return Result


def first_name(user):
    profile = user.get("profile") if user else None
    return profile["name"]
