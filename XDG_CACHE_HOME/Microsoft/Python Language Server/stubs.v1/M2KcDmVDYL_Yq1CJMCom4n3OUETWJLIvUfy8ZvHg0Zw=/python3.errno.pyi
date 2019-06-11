import builtins as _mod_builtins

E2BIG = 7
EACCES = 13
EADDRINUSE = 98
EADDRNOTAVAIL = 99
EADV = 68
EAFNOSUPPORT = 97
EAGAIN = 11
EALREADY = 114
EBADE = 52
EBADF = 9
EBADFD = 77
EBADMSG = 74
EBADR = 53
EBADRQC = 56
EBADSLT = 57
EBFONT = 59
EBUSY = 16
ECANCELED = 125
ECHILD = 10
ECHRNG = 44
ECOMM = 70
ECONNABORTED = 103
ECONNREFUSED = 111
ECONNRESET = 104
EDEADLK = 35
EDEADLOCK = 35
EDESTADDRREQ = 89
EDOM = 33
EDOTDOT = 73
EDQUOT = 122
EEXIST = 17
EFAULT = 14
EFBIG = 27
EHOSTDOWN = 112
EHOSTUNREACH = 113
EIDRM = 43
EILSEQ = 84
EINPROGRESS = 115
EINTR = 4
EINVAL = 22
EIO = 5
EISCONN = 106
EISDIR = 21
EISNAM = 120
EKEYEXPIRED = 127
EKEYREJECTED = 129
EKEYREVOKED = 128
EL2HLT = 51
EL2NSYNC = 45
EL3HLT = 46
EL3RST = 47
ELIBACC = 79
ELIBBAD = 80
ELIBEXEC = 83
ELIBMfig = 82
ELIBSCN = 81
ELNRNG = 48
ELOOP = 40
EMEDIUMTYPE = 124
EMFILE = 24
EMLINK = 31
EMSGSIZE = 90
EMULTIHOP = 72
ENAMETOOLONG = 36
ENAVAIL = 119
ENETDOWN = 100
ENETRESET = 102
ENETUNREACH = 101
ENFILE = 23
ENOANO = 55
ENOBUFS = 105
ENOCSI = 50
ENODATA = 61
ENODEV = 19
ENOENT = 2
ENOEXEC = 8
ENOKEY = 126
ENOLCK = 37
ENOLINK = 67
ENOMEDIUM = 123
ENOMEM = 12
ENOMSG = 42
ENONET = 64
ENOPKG = 65
ENOPROTOOPT = 92
ENOSPC = 28
ENOSR = 63
ENOSTR = 60
ENOSYS = 38
ENOTBLK = 15
ENOTCONN = 107
ENOTDIR = 20
ENOTEMPTY = 39
ENOTNAM = 118
ENOTRECOVERABLE = 131
ENOTSOCK = 88
ENOTSUP = 95
ENOTTY = 25
ENOTUNIQ = 76
ENXIO = 6
EOPNOTSUPP = 95
EOVERFLOW = 75
EOWNERDEAD = 130
EPERM = 1
EPFNOSUPPORT = 96
EPIPE = 32
EPROTO = 71
EPROTONOSUPPORT = 93
EPROTOTYPE = 91
ERANGE = 34
EREMCHG = 78
EREMOTE = 66
EREMOTEIO = 121
ERESTART = 85
ERFKILL = 132
EROFS = 30
ESHUTDOWN = 108
ESOCKTNOSUPPORT = 94
ESPIPE = 29
ESRCH = 3
ESRMNT = 69
ESTALE = 116
ESTRPIPE = 86
ETIME = 62
ETIMEDOUT = 110
ETOOMANYREFS = 109
ETXTBSY = 26
EUCLEAN = 117
EUNATCH = 49
EUSERS = 87
EWOULDBLOCK = 11
EXDEV = 18
EXFULL = 54
__doc__ = "This module makes available standard errno system symbols.\n\nThe value of each symbol is the corresponding integer value,\ne.g., on most systems, errno.ENOENT equals the integer 2.\n\nThe dictionary errno.errorcode maps numeric codes to symbol names,\ne.g., errno.errorcode[2] could be the string 'ENOENT'.\n\nSymbols that are not relevant to the underlying system are not defined.\n\nTo map error codes to error messages, use the function os.strerror(),\ne.g. os.strerror(2) could return 'No such file or directory'."
__name__ = 'errno'
__package__ = ''
errorcode = _mod_builtins.dict()
