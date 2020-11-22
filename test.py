from jnius import autoclass

Stack = autoclass('java.util.Stack')
stack = Stack()
stack.push('hello')
stack.push('world')

print(stack.pop()) # --> 'world'
print(stack.pop()) # --> 'hello'

version = autoclass('android.os.Build$VERSION')
base_os = version.BASE_OS

print(base_os)