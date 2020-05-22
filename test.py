# from pathdict import PathDict
# import superpy as sp
# import copy
# import sys


# # Dict for testing purposes
# users = {
# 	"total_users": 3,
# 	"premium_users": [1, 3],
# 	"users": {
# 		"1": {
# 			"name": "Joe",
# 			"age": 22,
# 		},
# 		"2": {
# 			"name": "Ben",
# 			"age": 49
# 		},
# 		"3": {
# 			"name": "Sue",
# 			"age": 32,
# 		},
# 	},
# 	"follows": [
# 		["Ben", "Sue"],
# 		["Joe", "Ben"],
# 		["Ben", "Joe"],
# 	]
# }



# @sp.test()
# def initialization():
# 	# Empty
# 	pd_empty = PathDict({})
# 	assert pd_empty.dict == {}
# 	# Wrong inits
# 	for wrong in ["", None, 1, [1]]:
# 		try:
# 			_ = PathDict(wrong)
# 			assert False
# 		except Exception:
# 			assert True
# 	# Init with PathDict
# 	init_pd = PathDict({"test": 1})
# 	pd_from_pd = PathDict(init_pd)
# 	assert init_pd == pd_from_pd
# 	assert init_pd.data is pd_from_pd.data
# 	# Init with dict
# 	init_dict = copy.deepcopy(users)
# 	pd = PathDict(init_dict)
# 	assert pd.data is pd.dict
# 	assert pd.dict is init_dict
# 	assert pd is not init_dict
# 	assert pd == init_dict
# 	assert pd["users"].dict is init_dict["users"]
# 	assert isinstance(pd["premium_users"], list)
# 	assert pd["premium_users"] is init_dict["premium_users"]
# 	# Deep copy behavior
# 	dc_pd = PathDict(users, deep_copy=True)
# 	assert dc_pd.dict is not users
# 	dc_pd_deepcopy = dc_pd.deepcopy
# 	assert dc_pd is not dc_pd_deepcopy


# @sp.test()
# def test_get_path():
# 	users_dict = copy.deepcopy(users)
# 	users_pd = PathDict(users_dict)
# 	assert users_pd["total_users"] == 3
# 	assert users_pd["users", "1", "name"] == "Joe"
# 	# Non existent but correct paths return None
# 	assert users_pd["users", "-1", "name"] is None
# 	# If value is not a dict, return that value
# 	assert isinstance(users_pd["follows"], list)
# 	# If value is a dict, return a PathDict
# 	assert isinstance(users_pd["users"], PathDict)
# 	assert users_pd["users"].dict is users_dict["users"]
# 	# Wrong path accesses, eg. get key on list, raise an exception
# 	try:
# 		_ = users_pd["follows", 0]
# 		assert False
# 	except BaseException:
# 		assert True

# @sp.test()
# def test_filter():
# 	users_pd = PathDict(users, deep_copy=True)

# 	users_filtered = users_pd.filtered("users", f=lambda k, v: v["age"] <= 30)
# 	assert users_filtered["users"] == {
# 		"1": {
# 			"age": 22,
# 			"name": "Joe"
# 		}
# 	}
# 	assert isinstance(users_filtered, PathDict)

# 	premium_users = users_pd["users"].filtered(f=lambda k, v: int(k) in users_pd["premium_users"])
# 	assert isinstance(premium_users, PathDict)

# 	assert premium_users == {
# 		"1": {
# 			"age": 22,
# 			"name": "Joe"
# 		},
# 		"3": {
# 			"age": 32,
# 			"name": "Sue"
# 		}
# 	}

# 	follows_includes_joe = users_pd.filtered("follows", f=lambda e: "Joe" in e)
# 	assert isinstance(follows_includes_joe["follows"], list)
# 	assert follows_includes_joe["follows"] == [
# 		["Joe", "Ben"],
# 		["Ben", "Joe"],
# 	]







# @sp.test()
# def test_PathDict():
# 	d = {
# 		"total_users": 3,
# 		"premium_users": [1, 3],
# 		"users": {
# 			"1": {"name": "Joe", "age": 22},
# 			"2": {"name": "Ben", "age": 49},
# 			"3": {"name": "Sue", "age": 32},
# 		},
# 		"follows": [
# 			["Ben", "Sue"],
# 			["Joe", "Ben"],
# 			["Ben", "Joe"],
# 		]
# 	}
# 	o = PathDict(d)
# 	# Getting attributes
# 	assert o["total_users"] == 3
# 	assert o["not_exists"] == None
# 	assert o["users"] == {
# 		"1": {"name": "Joe", "age": 22},
# 		"2": {"name": "Ben", "age": 49},
# 		"3": {"name": "Sue", "age": 32}}
# 	assert o["users", "1"] == {"name": "Joe", "age": 22}
# 	assert o["users", "3", "name"] == "Sue"
# 	assert o["follows"][0] == ["Ben", "Sue"]
# 	# Setting attributes
# 	o["total_users"] = 4
# 	assert o["total_users"] == 4
# 	o["users", "3", "age"] = 99
# 	assert o["users", "3", "age"] == 99
# 	o["users", "4"] = {"name": "Ron", "age": 62}
# 	assert o["users", "4"] == {"name": "Ron", "age": 62}
# 	o["1", "1", "1", "1"] = 1
# 	assert o["1", "1", "1"] == {"1": 1}
# 	# Apply functions
# 	o["follows"] = lambda x: [list(reversed(e)) for e in x]
# 	assert o["follows"] == [
# 		["Sue", "Ben"],
# 		["Ben", "Joe"],
# 		["Joe", "Ben"]]

# 	assert o.dict == {
# 		"1": {"1": {"1": {"1": 1}}},
# 		"total_users": 4,
# 		"premium_users": [1, 3],
# 		"users": {
# 			"1": {"name": "Joe", "age": 22},
# 			"2": {"name": "Ben", "age": 49},
# 			"3": {"name": "Sue", "age": 99},
# 			"4": {"name": "Ron", "age": 62},
# 		},
# 		"follows": [
# 			["Sue", "Ben"],
# 			["Ben", "Joe"],
# 			["Joe", "Ben"]]
# 	}