# TODO:
# - add support for ingres, msql, oracle
#
# Conditional build:
%bcond_without	firebird	# don't build Firebird driver
%bcond_without	freetds		# don't build FreeTDS driver
%bcond_without	mysql		# don't build MySQL driver
%bcond_without	pgsql		# don't build PostgreSQL driver
%bcond_without	sqlite		# don't build sqlite driver
%bcond_without	sqlite3		# don't build sqlite3 driver
%bcond_with	doc			# don't build documentation
#
%define dbiver	0.9.0
Summary:	Database Independent Abstraction Layer for C
Summary(pl.UTF-8):	Warstwa DBI dla C
Name:		libdbi-drivers
%define	_snap	20100921
Version:	0.9.0
Release:	0.%{_snap}.2
License:	LGPL v2+
Group:		Libraries
#Source0:	http://dl.sourceforge.net/libdbi-drivers/libdbi-drivers-%{version}-1.tar.gz
Source0:	%{name}-%{_snap}.tar.gz
# Source0-md5:	3e3b1df63ab59f9246111db7fbad8310
Patch0:		%{name}-sqlite3_libs.patch
URL:		http://libdbi-drivers.sourceforge.net/
%if %{with doc}
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-style-dsssl
BuildRequires:	jadetex
BuildRequires:	openjade
BuildRequires:	texlive-fonts-ams
BuildRequires:	texlive-fonts-marvosym
BuildRequires:	texlive-fonts-stmaryrd
BuildRequires:	texlive-fonts-type1-urw
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-latex-ams
BuildRequires:	texlive-latex-extend
BuildRequires:	texlive-latex-wasysym
BuildRequires:	texlive-xetex
BuildRequires:	texlive-xmltex
%endif
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

%description -l pl.UTF-8
libdbi jest implementacją w C warstwy abstrakcyjnej niezależnej od
bazy danych, podobnej do warstwy DBI/DBD w Perlu. Używając tego
środowiska programista może za pomocą jednego, wspólnego kodu
odwoływać się do wielu różnych baz danych, także jednocześnie.

%package firebird
Summary:	Firebird plugin for libdbi
Summary(pl.UTF-8):	Wtyczka Firebird dla libdbi
Group:		Libraries
Requires:	libdbi >= %{dbiver}
Provides:	libdbi-dbd = %{version}-%{release}

%description firebird
This plugin provides connectivity to Firebird database servers through
the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%description firebird -l pl.UTF-8
Ta wtyczka daje możliwość łączenia się z serwerami Firebird poprzez
bibliotekę libdbi. Zmiana używanej wtyczki nie wymaga rekompilacji ani
zmiany źródeł programu.

%package freetds
Summary:	FreeTDS plugin for libdbi
Summary(pl.UTF-8):	Wtyczka FreeTDS dla libdbi
Group:		Libraries
Requires:	libdbi >= %{dbiver}
Provides:	libdbi-dbd = %{version}-%{release}

%description freetds
This plugin provides connectivity to MS SQL/Sybase database servers
through the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%description freetds -l pl.UTF-8
Ta wtyczka daje możliwość łączenia się z serwerami MS SQL/Sybase
poprzez bibliotekę libdbi. Zmiana używanej wtyczki nie wymaga
rekompilacji ani zmiany źródeł programu.

%package mysql
Summary:	MySQL plugin for libdbi
Summary(pl.UTF-8):	Wtyczka MySQL dla libdbi
Group:		Libraries
Requires:	libdbi >= %{dbiver}
Provides:	libdbi-dbd = %{version}-%{release}
Obsoletes:	libdbi-dbd-mysql

%description mysql
This plugin provides connectivity to MySQL database servers through
the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%description mysql -l pl.UTF-8
Ta wtyczka daje możliwość łączenia się z serwerami MySQL poprzez
bibliotekę libdbi. Zmiana używanej wtyczki nie wymaga rekompilacji ani
zmiany źródeł programu.

%package pgsql
Summary:	PostgreSQL plugin for libdbi
Summary(pl.UTF-8):	Wtyczka PostgreSQL dla libdbi
Group:		Libraries
Requires:	libdbi >= %{dbiver}
Provides:	libdbi-dbd = %{version}-%{release}
Obsoletes:	libdbi-dbd-pgsql

%description pgsql
This plugin provides connectivity to PostgreSQL database servers
through the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%description pgsql -l pl.UTF-8
Ta wtyczka daje możliwość łączenia się z serwerami PostgreSQL poprzez
bibliotekę libdbi. Zmiana używanej wtyczki nie wymaga rekompilacji ani
zmiany źródeł programu.

%package sqlite
Summary:	SQLite plugin for libdbi
Summary(pl.UTF-8):	Wtyczka SQLite dla libdbi
Group:		Libraries
Requires:	libdbi >= %{dbiver}
Provides:	libdbi-dbd = %{version}-%{release}

%description sqlite
This plugin provides connectivity to SQLite engine
through the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%description sqlite -l pl.UTF-8
Ta wtyczka daje możliwość łączenia się z silnikiem SQLite poprzez
bibliotekę libdbi. Zmiana używanej wtyczki nie wymaga rekompilacji ani
zmiany źródeł programu.

%package sqlite3
Summary:	SQLite3 plugin for libdbi
Summary(pl.UTF-8):	Wtyczka SQLite3 dla libdbi
Group:		Libraries
Requires:	libdbi >= %{dbiver}
Provides:	libdbi-dbd = %{version}-%{release}

%description sqlite3
This plugin provides connectivity to SQLite3 engine through the libdbi
database independent abstraction layer. Switching a program's plugin
does not require recompilation or rewriting source code.

%description sqlite3 -l pl.UTF-8
Ta wtyczka daje możliwość łączenia się z silnikiem SQLite3 poprzez
bibliotekę libdbi. Zmiana używanej wtyczki nie wymaga rekompilacji ani
zmiany źródeł programu.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	%{!?with_doc:--disable-docs} \
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
	--enable-mysql-threadsafe \
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
%if %{with sqlite3}
	--with-sqlite3 \
	--with-sqlite3-libdir=%{_libdir} \
	--with-sqlite3-incdir=%{_includedir} \
%endif
	--with-dbi-incdir=%{_includedir} \
	--with-dbi-libdir=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/dbd

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/dbd/lib*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

#%files common
#%doc AUTHORS ChangeLog NEWS README README.encodings TODO

%if %{with firebird}
%files firebird
%defattr(644,root,root,755)
%doc drivers/firebird/{AUTHORS,README,TODO%{?with_doc:,dbd_firebird}}
%attr(755,root,root) %{_libdir}/dbd/libdbdfirebird.so
%endif

%if %{with freetds}
%files freetds
%defattr(644,root,root,755)
%doc drivers/freetds/README
%attr(755,root,root) %{_libdir}/dbd/libdbdfreetds.so
%endif

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
%doc drivers/mysql/{AUTHORS,README,TODO%{?with_doc:,dbd_mysql.pdf,dbd_mysql}}
%attr(755,root,root) %{_libdir}/dbd/libdbdmysql.so
%endif

%if %{with pgsql}
%files pgsql
%defattr(644,root,root,755)
%doc drivers/pgsql/{AUTHORS,README,TODO%{?with_doc:,dbd_pgsql.pdf,dbd_pgsql}}
%attr(755,root,root) %{_libdir}/dbd/libdbdpgsql.so
%endif

%if %{with sqlite}
%files sqlite
%defattr(644,root,root,755)
%doc drivers/sqlite/{AUTHORS,README,TODO%{?with_doc:,dbd_sqlite.pdf,dbd_sqlite}}
%attr(755,root,root) %{_libdir}/dbd/libdbdsqlite.so
%endif

%if %{with sqlite3}
%files sqlite3
%defattr(644,root,root,755)
%doc drivers/sqlite3/{AUTHORS,README,TODO%{?with_doc:,dbd_sqlite3.pdf,dbd_sqlite3}}
%attr(755,root,root) %{_libdir}/dbd/libdbdsqlite3.so
%endif
