%{?_javapackages_macros:%_javapackages_macros}
Name:             hawtjni
Version:          1.10
Release:          3.1
Summary:          Code generator that produces the JNI code
Group:		  Development/Java
License:          ASL 2.0 and EPL and BSD
URL:              http://hawtjni.fusesource.org/
BuildArch:        noarch

Source0:          https://github.com/fusesource/hawtjni/archive/hawtjni-project-%{version}.tar.gz

Patch0:           0001-Fix-shading-and-remove-unneeded-modules.patch
Patch1:           0002-Fix-xbean-compatibility.patch
Patch2:           0003-Remove-plexus-maven-plugin-dependency.patch
Patch3:           0004-Remove-eclipse-plugin.patch

BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-plugin-plugin
BuildRequires:    maven-surefire-report-plugin
BuildRequires:    maven-project-info-reports-plugin
BuildRequires:    maven-plugin-jxr
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-clean-plugin
BuildRequires:    plexus-containers-component-metadata
BuildRequires:    log4j
BuildRequires:    junit
BuildRequires:    fusesource-pom
BuildRequires:    xbean

Requires:         autoconf
Requires:         automake
Requires:         libtool

%description
HawtJNI is a code generator that produces the JNI code needed to
implement java native methods. It is based on the jnigen code generator
that is part of the SWT Tools project which is used to generate all the
JNI code which powers the eclipse platform.

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%package runtime
Summary:          HawtJNI Runtime

%description runtime
This package provides API that projects using HawtJNI should build
against.

%package -n maven-hawtjni-plugin
Summary:          Use HawtJNI from a maven plugin

%description -n maven-%{name}-plugin
This package allows to use HawtJNI from a maven plugin.

%prep
%setup -q -n hawtjni-hawtjni-project-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Ready to replace patch0
# %pom_disable_module hawtjni-example
# %pom_disable_module hawtjni-website
# %pom_add_dep "org.apache.maven:maven-compat:3.0.3" maven-hawtjni-plugin/pom.xml
# %pom_remove_plugin ":maven-shade-plugin" hawtjni-generator/pom.xml

%mvn_package ":hawtjni-runtime" runtime
%mvn_package ":maven-hawtjni-plugin" maven-plugin

%pom_xpath_set "pom:groupId[text()='asm']" org.ow2.asm hawtjni-generator

%build
%mvn_build

%install
%mvn_install

%files runtime -f .mfiles-runtime
%dir %{_javadir}/%{name}
%doc readme.md license.txt changelog.md

%files -f .mfiles

%files javadoc -f .mfiles-javadoc
%doc license.txt

%files -n maven-hawtjni-plugin -f .mfiles-maven-plugin

%changelog
* Fri Nov 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.10-3
- Spit runtime into subpackage
- Resolves: rhbz#1166607

* Mon Jun  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.10-2
- Add requires on autoconf, automake, libtool

* Mon Jun  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.10-1
- Update to upstream version 1.10

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-4
- Migrate BuildRequires from junit4 to junit

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-3
- Remove BuildRequires on maven-surefire-provider-junit4

* Thu Mar  6 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-2
- Update to ASM4
- Resolves: rhbz#1073507

* Wed Sep 18 2013 Marek Goldmann <mgoldman@redhat.com> - 1.9-1
- Upstream release 1.9
- hawtjni: missing barriers in cache initialization, RHBZ#957181

* Tue Aug 06 2013 Marek Goldmann <mgoldman@redhat.com> - 1.8-3
- New guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Marek Goldmann <mgoldman@redhat.com> - 1.8-1
- Upstream release 1.8

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-5
- Remove unneeded BR: maven-idea-plugin

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.6-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-2
- Replace asm2 requires with objectweb-asm
- Resolves: rhbz#902674

* Fri Sep 07 2012 gil cattaneo <puntogil@libero.it> 1.6-1
- Upstream release 1.6

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.5-3
- Remove eclipse plugin from BuildRequires

* Thu Jan 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.5-2
- Replace plexus-maven-plugin with plexus-containers implementation

* Sun Jan 15 2012 Marek Goldmann <mgoldman@redhat.com> 1.5-1
- Upstream release 1.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 10 2011 Marek Goldmann <mgoldman@redhat.com> 1.3-1
- Upstream release 1.3

* Fri Jul 29 2011 Marek Goldmann <mgoldman@redhat.com> 1.2-1
- Upstream release 1.2
- Moved to new depmap macro

* Mon May 30 2011 Marek Goldmann <mgoldman@redhat.com> 1.1-4
- Removed maven-shade-plugin dependency

* Mon May 30 2011 Marek Goldmann <mgoldman@redhat.com> 1.1-3
- Split maven-hawtjni-plugin into new package
- Fixed license
- Fixed summary
- Using xz to compress source code

* Sun May 29 2011 Marek Goldmann <mgoldman@redhat.com> 1.1-2
- Added maven-hawtjni-plugin

* Fri May 27 2011 Marek Goldmann <mgoldman@redhat.com> 1.1-1
- Initial packaging
