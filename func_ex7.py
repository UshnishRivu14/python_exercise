def st_name(name,age):
    print(name,age)

print("Calling with old function")
st_name('semma',27)

ft_name = st_name
print("Calling with new function")

ft_name("emma",26)