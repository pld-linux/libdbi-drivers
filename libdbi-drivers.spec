%bcond_without mysql  # don't build mysql driver
%bcond_without pgsql  # don't build postgresql driver
%bcond_without sqlite # don't build sqlite driver
%define dbiver                  0.7.1
Summary:	Database Independent Abstraction Layer for C
Summary(pl):	Warstwa DBI dla C
Name:		libdbi-drivers
Version:	0.7.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libdbi-drivers/libdbi-drivers-%{version}.tar.gz
# Source0-md5:	4a523d28b53934cdd6bf1fadf0bfc6b9
Patch0:		%{name}-opt.patch
URL:		http://libdbi-drivers.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libdbi-devel >= %{dbiver}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_pgsql:BuildRequires:	postgresql-devel}
%{?with_sqlite:BuildRequires:	sqlite-devel}
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

%prep
%setup -q
%patch -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	%{?with_sqlite:--with-sqlite} \
	%{?with_mysql:--with-mysql} \
	%{?with_pgsql:--with-pgsql} \
	--with-dbi-incdir=%{_includedir} 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/dbd

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
%doc drivers/mysql/*.pdf drivers/mysql/dbd_mysql
%attr(755,root,root) %{_libdir}/dbd/libmysql.so
%endif

%if %{with pgsql}
%files pgsql
%defattr(644,root,root,755)
%doc drivers/pgsql/*.pdf drivers/pgsql/dbd_pgsql
%attr(755,root,root) %{_libdir}/dbd/libpgsql.so
%endif

%if %{with sqlite}
%files sqlite
%defattr(644,root,root,755)
%doc drivers/sqlite/*.pdf drivers/sqlite/dbd_sqlite
%{_libdir}/dbd/libsqlite.so
%endif
