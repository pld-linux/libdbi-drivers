#
# Conditional build:
%bcond_without	firebird	# don't build Firebird driver
%bcond_without	freetds		# don't build FreeTDS driver
%bcond_without	mysql		# don't build MySQL driver
%bcond_without	pgsql		# don't build PostgreSQL driver
%bcond_without	sqlite		# don't build sqlite driver
%bcond_without	sqlite3		# don't build sqlite3 driver
#
%define dbiver	0.8.1
Summary:	Database Independent Abstraction Layer for C
Summary(pl):	Warstwa DBI dla C
Name:		libdbi-drivers
Version:	0.8.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libdbi-drivers/libdbi-drivers-%{version}.tar.gz
# Source0-md5:	bca4dd6184e3e78676c35eb9a7ae1186
Patch0:		%{name}-opt.patch
URL:		http://libdbi-drivers.sourceforge.net/
%{?with_firebird:BuildRequires:	Firebird-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_freetds:BuildRequires:	freetds-devel}
BuildRequires:	libtool
BuildRequires:	libdbi-devel >= %{dbiver}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_pgsql:BuildRequires:	postgresql-devel}
%{?with_sqlite:BuildRequires:	sqlite-devel}
%{?with_sqlite3:BuildRequires:	sqlite3-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdbi implements a database-independent abstraction layer in C,
similar to the DBI/DBD layer in Perl. Writing one generic set of code,
programmers can leverage the power of multiple databases and multiple
simultaneous database connections by using this framework.

%description -l pl
libdbi jest implementacj± w C warstwy abstrakcyjnej niezale¿nej od
bazy danych, podobnej do warstwy DBI/DBD w Perlu. U¿ywaj±c tego
¶rodowiska programista mo¿e za pomoc± jednego, wspólnego kodu
odwo³ywaæ siê do wielu ró¿nych baz danych, tak¿e jednocze¶nie.

%package firebird
Summary:	Firebird plugin for libdbi
Summary(pl):	Wtyczka Firebird dla libdbi
Group:		Libraries
Requires:	libdbi >= %{dbiver}
Provides:	libdbi-dbd = %{version}-%{release}

%description firebird
This plugin provides connectivity to Firebird database servers through
the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%description firebird -l pl
Ta wtyczka daje mo¿liwo¶æ ³±czenia siê z serwerami Firebird poprzez
bibliotekê libdbi. Zmiana u¿ywanej wtyczki nie wymaga rekompilacji ani
zmiany ¼róde³ programu.

%package freetds
Summary:	FreeTDS plugin for libdbi
Summary(pl):	Wtyczka FreeTDS dla libdbi
Group:		Libraries
Requires:	libdbi >= %{dbiver}
Provides:	libdbi-dbd = %{version}-%{release}

%description freetds
This plugin provides connectivity to MS SQL/Sybase database servers
through the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%description freetds -l pl
Ta wtyczka daje mo¿liwo¶æ ³±czenia siê z serwerami MS SQL/Sybase
poprzez bibliotekê libdbi. Zmiana u¿ywanej wtyczki nie wymaga
rekompilacji ani zmiany ¼róde³ programu.

%package mysql
Summary:	MySQL plugin for libdbi
Summary(pl):	Wtyczka MySQL dla libdbi
Group:		Libraries
Requires:	libdbi >= %{dbiver}
Provides:	libdbi-dbd = %{version}-%{release}
Obsoletes:	libdbi-dbd-mysql

%description mysql
This plugin provides connectivity to MySQL database servers through
the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%description mysql -l pl
Ta wtyczka daje mo¿liwo¶æ ³±czenia siê z serwerami MySQL poprzez
bibliotekê libdbi. Zmiana u¿ywanej wtyczki nie wymaga rekompilacji ani
zmiany ¼róde³ programu.

%package pgsql
Summary:	PostgreSQL plugin for libdbi
Summary(pl):	Wtyczka PostgreSQL dla libdbi
Group:		Libraries
Requires:	libdbi >= %{dbiver}
Provides:	libdbi-dbd = %{version}-%{release}
Obsoletes:	libdbi-dbd-pgsql

%description pgsql
This plugin provides connectivity to PostgreSQL database servers
through the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%description pgsql -l pl
Ta wtyczka daje mo¿liwo¶æ ³±czenia siê z serwerami PostgreSQL poprzez
bibliotekê libdbi. Zmiana u¿ywanej wtyczki nie wymaga rekompilacji ani
zmiany ¼róde³ programu.

%package sqlite
Summary:	SQLite plugin for libdbi
Summary(pl):	Wtyczka SQLite dla libdbi
Group:		Libraries
Requires:	libdbi >= %{dbiver}
Provides:	libdbi-dbd = %{version}-%{release}

%description sqlite
This plugin provides connectivity to SQLite engine
through the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%description sqlite -l pl
Ta wtyczka daje mo¿liwo¶æ ³±czenia siê z silnikiem SQLite poprzez
bibliotekê libdbi. Zmiana u¿ywanej wtyczki nie wymaga rekompilacji ani
zmiany ¼róde³ programu.

%package sqlite3
Summary:	SQLite3 plugin for libdbi
Summary(pl):	Wtyczka SQLite3 dla libdbi
Group:		Libraries
Requires:	libdbi >= %{dbiver}
Provides:	libdbi-dbd = %{version}-%{release}

%description sqlite3
This plugin provides connectivity to SQLite3 engine through the libdbi
database independent abstraction layer. Switching a program's plugin
does not require recompilation or rewriting source code.

%description sqlite3 -l pl
Ta wtyczka daje mo¿liwo¶æ ³±czenia siê z silnikiem SQLite3 poprzez
bibliotekê libdbi. Zmiana u¿ywanej wtyczki nie wymaga rekompilacji ani
zmiany ¼róde³ programu.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static \
%if %{with firebird}
	--with-firebird \
	--with-firebird-libdir=%{_libdir} \
	--with-firebird-incdir=%{_includedir} \
%endif
%if %{with freetds}
	--with-freetds \
	--with-freetds-libdir=%{_libdir} \
	--with-freetds-incdir=%{_includedir} \
%endif
%if %{with mysql}
	--with-mysql \
	--with-mysql-libdir=%{_libdir} \
	--with-mysql-incdir=%{_includedir} \
%endif
%if %{with pgsql}
	--with-pgsql \
	--with-pgsql-libdir=%{_libdir} \
	--with-pgsql-incdir=%{_includedir} \
%endif
%if %{with sqlite}
	--with-sqlite \
	--with-sqlite-libdir=%{_libdir} \
	--with-sqlite-incdir=%{_includedir} \
%endif
%if %{with sqlite}
	--with-sqlite3 \
	--with-sqlite3-libdir=%{_libdir} \
	--with-sqlite3-incdir=%{_includedir} \
%endif
	--with-dbi-incdir=%{_includedir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/dbd

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/dbd/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with firebird}
%files firebird
%defattr(644,root,root,755)
%doc drivers/firebird/{AUTHORS,README,TODO}
%attr(755,root,root) %{_libdir}/dbd/libfirebird.so
%endif

%if %{with freetds}
%files freetds
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dbd/libfreetds.so
%endif

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
%doc drivers/mysql/{AUTHORS,README,TODO,*.pdf,dbd_mysql}
%attr(755,root,root) %{_libdir}/dbd/libmysql.so
%endif

%if %{with pgsql}
%files pgsql
%defattr(644,root,root,755)
%doc drivers/pgsql/{AUTHORS,README,TODO,*.pdf,dbd_pgsql}
%attr(755,root,root) %{_libdir}/dbd/libpgsql.so
%endif

%if %{with sqlite}
%files sqlite
%defattr(644,root,root,755)
%doc drivers/sqlite/{AUTHORS,README,TODO,*.pdf,dbd_sqlite}
%{_libdir}/dbd/libsqlite.so
%endif

%if %{with sqlite3}
%files sqlite3
%defattr(644,root,root,755)
%doc drivers/sqlite3/{AUTHORS,README,TODO,*.pdf,dbd_sqlite3}
%{_libdir}/dbd/libsqlite3.so
%endif
