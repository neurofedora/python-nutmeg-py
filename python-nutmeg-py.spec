%global modname nutmeg-py
%global commit 433206e8663916889957673af7f2bfda60e47b90
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{modname}
Version:        0.1a
Release:        1%{?dist}
Summary:        Neurodynamic Utility Toolbox for M/EEG
License:        BSD
URL:            http://nutmeg.berkeley.edu  
Source0:        https://github.com/miketrumpis/nutmeg-py.git/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

%description
NUTMEG (Neurodynamic Utility Toolbox for Magnetoencephalo
and Electroencephalo Graphy) is an MEG/EEG analysis toolbox
x for reconstructing the spatiotemporal dynamics of neural 
activations and overlaying them onto structural MR images. 
The toolbox runs under MATLAB in conjunction with SPM8 and 
can be used with the Linux/UNIX, Mac OS X, and even Windows 
platforms. NUTMEG is open source and distributed under a 
BSD-style license. The developers are current and former 
members and collaborators of the UCSF Biomagnetic Imaging 
Laboratory.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel

%description -n python2-%{modname}
NUTMEG (Neurodynamic Utility Toolbox for Magnetoencephalo
and Electroencephalo Graphy) is an MEG/EEG analysis toolbox
x for reconstructing the spatiotemporal dynamics of neural 
activations and overlaying them onto structural MR images. 
The toolbox runs under MATLAB in conjunction with SPM8 and 
can be used with the Linux/UNIX, Mac OS X, and even Windows 
platforms. NUTMEG is open source and distributed under a 
BSD-style license. The developers are current and former 
members and collaborators of the UCSF Biomagnetic Imaging 
Laboratory.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel

%description -n python3-%{modname}
NUTMEG (Neurodynamic Utility Toolbox for Magnetoencephalo
and Electroencephalo Graphy) is an MEG/EEG analysis toolbox
x for reconstructing the spatiotemporal dynamics of neural 
activations and overlaying them onto structural MR images. 
The toolbox runs under MATLAB in conjunction with SPM8 and 
can be used with the Linux/UNIX, Mac OS X, and even Windows 
platforms. NUTMEG is open source and distributed under a 
BSD-style license. The developers are current and former 
members and collaborators of the UCSF Biomagnetic Imaging 
Laboratory.

Python 3 version.

%prep
%autosetup -n %{modname}-%{commit}


%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
nosetests-%{python2_version} -v
nosetests-%{python3_version} -v

%files -n python2-%{modname}
%{python2_sitearch}/%{modname}*

%files -n python3-%{modname}
%{python3_sitearch}/%{modname}*

%changelog
* Thu Nov  5 2015 Adrian Alves <alvesadrian@fedoraproject.org> 0.1-a-1
- Initial build 
