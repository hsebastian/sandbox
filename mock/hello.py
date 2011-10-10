from mock import Mock

x = {'hello': "Hello World"}
xmock = Mock(x)
xmock.hello()

f = xmock.foo
f
f()

