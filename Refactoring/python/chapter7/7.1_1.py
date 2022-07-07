organization = {
    "name": "애크미 구스베리",
    "country": "GB"
}


def get_raw_data_of_organization():
    return {
        "name": "애크미 구스베리",
        "country": "GB"
    }


## client
result = get_raw_data_of_organization()["name"]
get_raw_data_of_organization()["name"] = "tttnewName"
