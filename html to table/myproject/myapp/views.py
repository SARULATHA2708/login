from django.shortcuts import render, redirect
from .db import users_collection  # This is your MongoDB collection
from bson.objectid import ObjectId
from django.contrib import messages

def collectdata(request):
    if request.method == "POST":
        newentry = {
            "name": request.POST["name"],
            "email": request.POST["email"],
            "age": int(request.POST["age"])
        }
        users_collection.insert_one(newentry)  # <- use correct name
        return redirect("viewdata")
    return render(request, "form.html")

def viewdata(request):
    data = list(users_collection.find())  # <- use correct name
    for item in data:
        item["id"] = str(item["_id"])
    return render(request, "table.html", {"data": data})

def editdata(request, id):
    entry = users_collection.find_one({"_id": ObjectId(id)})  # <- use correct name
    if not entry:
        return redirect("viewdata")
    if request.method == "POST":
        updated_data = {
            "name": request.POST["name"],
            "email": request.POST["email"],
            "age": int(request.POST["age"])
        }
        users_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})  # <- use correct name
        return redirect("viewdata")
    entry["id"] = str(entry["_id"])
    return render(request, "edit.html", {"person": entry})

def delete(request, id):
    entry = users_collection.find_one({"_id": ObjectId(id)})  # <- use correct name
    if not entry:
        return redirect("viewdata")
    if request.method == "POST" and "confirm" in request.POST:
        users_collection.delete_one({"_id": ObjectId(id)})  # <- use correct name
        return redirect("viewdata")
    entry["id"] = str(entry["_id"])
    return render(request, "delete.html", {"person": entry})
