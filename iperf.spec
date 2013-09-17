Name: iperf
Version: 2.0.5
Release: 4
Summary: Measurement tool for TCP/UDP bandwidth performance
License: BSD
Group: Applications/Internet
URL: http://sourceforge.net/projects/iperf
Source: %{name}-%{version}.tar.gz
Patch1:	0001-iperf-2.0.5-debuginfo.patch
Patch2:	0002-iperf-2.0.5-tcpdual.patch

%description
Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning of
various parameters and UDP characteristics. Iperf reports bandwidth, delay
jitter, datagram loss.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%make_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README doc/*.gif doc/*.html
%{_bindir}/iperf
%{_mandir}/man*/*
