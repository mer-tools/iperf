Name: iperf
Version: 2.0.5
Release: 3%{?dist}
Summary: Measurement tool for TCP/UDP bandwidth performance
License: BSD
Group: Applications/Internet
URL: http://sourceforge.net/projects/iperf
Source: http://sourceforge.net/projects/iperf/files/%{name}-%{version}.tar.gz
Patch1:	0001-iperf-2.0.5-debuginfo.patch
Patch2:	0002-iperf-2.0.5-tcpdual.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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

%changelog
* Mon Nov 28 2011 Gabriel Somlo <somlo at cmu.edu> 2.0.5-3
- include man page with build (BZ 756794)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 21 2010 Gabriel Somlo <somlo at cmu.edu> 2.0.5-1
- update to 2.0.5

* Tue Dec 01 2009 Gabriel Somlo <somlo at cmu.edu> 2.0.4-4
- patched to current svn trunk to address performance issues (#506884)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Gabriel Somlo <somlo at cmu.edu> 2.0.4-1
- update to 2.0.4
- patch to avoid tcp/dualtest server from quitting (bugzilla #449796), also submitted to iperf sourceforge ticket tracker (#1983829)

* Sat Oct 27 2007 Gabriel Somlo <somlo at cmu.edu> 2.0.2-4
- replace usleep with sched_yield to avoid hogging CPU (bugzilla #355211)

* Mon Jan 29 2007 Gabriel Somlo <somlo at cmu.edu> 2.0.2-3
- patch to prevent removal of debug info by ville.sxytta(at)iki.fi

* Fri Sep 08 2006 Gabriel Somlo <somlo at cmu.edu> 2.0.2-2
- rebuilt for FC6MassRebuild

* Wed Apr 19 2006 Gabriel Somlo <somlo at cmu.edu> 2.0.2-1
- initial build for fedora extras (based on Dag Wieers SRPM)
- fixed license tag: BSD (U. of IL / NCSA), not GPL
