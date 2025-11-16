# MyMusic Maestro

## [COM1025 - Databases, Networks and the Web](https://catalogue.surrey.ac.uk/2022-3/module/COM1025) | 2022/3

[![Grade](https://img.shields.io/badge/Grade-73%25-brightgreen)](https://github.com/BipinJungRai/MyMusicMaestro)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-4.2.6-green.svg)](https://www.djangoproject.com/)
[![University](https://img.shields.io/badge/University-Surrey-green.svg)](https://www.surrey.ac.uk/)

## 📋 Project Overview

This repository contains a **full-stack web application** developed for the **[COM1025 - Databases, Networks and the Web](https://catalogue.surrey.ac.uk/2022-3/module/COM1025)** module coursework at the University of Surrey (2022/3). The project is a music album catalog and management system built with Django, achieving a coursework grade of **73%**.

### Objective

Develop a database-driven web application that allows users to:
- **Browse and search** music albums
- **Manage album information** with full CRUD operations
- **Create and manage** song tracklists for albums
- **User authentication** with personalized accounts
- **Social features** including comments and recommendations

---

## 🎯 Problem Statement

Music enthusiasts and collectors need an organized platform to catalog and manage their album collections. This project aims to:

1. Create a comprehensive album database with detailed metadata
2. Implement user authentication and personalized features
3. Build an intuitive interface for album and song management
4. Enable social interaction through comments and recommendations
5. Support internationalization for multi-language accessibility

---

## 🗄️ Database Schema

### Models Implemented

#### 1. Album Model
- **Fields**:
  - `cover_art`: ImageField (optional, with default)
  - `title`: CharField (required, non-unique)
  - `description`: TextField (optional)
  - `artist`: CharField (required)
  - `price`: DecimalField (validated positive, default 0.00)
  - `format`: CharField with choices (Digital download, CD, Vinyl)
  - `release_date`: DateField (supports future releases up to 3 years)
- **Relationships**:
  - Many-to-Many with `Song`
  - Many-to-Many with `Comment`

#### 2. Song Model
- **Fields**:
  - `title`: CharField (required)
  - `running_time`: IntegerField (seconds)
- **Relationships**:
  - Many-to-Many with `Album`

#### 3. User Model (Custom)
- **Extends**: Django's AbstractUser
- **Fields**:
  - `username`: CharField (unique, optional)
  - `password`: CharField (required)
  - `display_name`: CharField (optional)
- **Relationships**:
  - Many-to-Many with `Comment`
  - Permissions and Groups

#### 4. Comment Model
- **Fields**:
  - `text`: TextField (required)
- **Relationships**:
  - ForeignKey to `User` (CASCADE)
  - ForeignKey to `Album` (CASCADE)

---

## 🌐 Features

### User Features
- ✅ **Authentication System**: Login/logout with Django authentication
- ✅ **User Accounts**: Personalized account page showing user comments
- ✅ **Album Browsing**: View all albums with cover art and metadata
- ✅ **Search Functionality**: Search albums by title
- ✅ **Album Details**: Detailed view with comments from all users
- ✅ **Recommend to Friend**: Email recommendation feature

### Admin/Management Features
- ✅ **CRUD Operations**: Create, Read, Update, Delete albums
- ✅ **Image Upload**: Album cover art with automatic file handling
- ✅ **Song Management**: Add/remove songs from albums via checkbox interface
- ✅ **Tracklist Editor**: Manage album tracklists dynamically
- ✅ **Comment Display**: View user comments on albums

### Technical Features
- ✅ **Internationalization (i18n)**: Full translation support with .po files
- ✅ **Data Seeding**: Custom management command to populate database
- ✅ **Responsive Design**: Bootstrap 5 integration
- ✅ **Static Files**: Custom CSS with sidebar navigation
- ✅ **Media Handling**: User-uploaded files with default fallbacks
- ✅ **Form Validation**: Server-side validation with Django Forms

---

## 📁 Repository Structure

```
MyMusicMaestro/
│
├── MyMusicMaestro/              # Django project configuration
│   ├── settings.py              # Project settings
│   ├── urls.py                  # URL routing
│   └── wsgi.py                  # WSGI configuration
│
├── app_album_viewer/            # Album management app
│   ├── models.py                # Database models (Album, Song, User, Comment)
│   ├── views.py                 # View logic for album features
│   ├── forms.py                 # Django forms (AlbumForm, SongForm)
│   ├── urls.py                  # URL routing for album views
│   ├── tests.py                 # Comprehensive test suite
│   ├── admin.py                 # Django admin configuration
│   ├── templates/               # Album-specific templates
│   │   ├── albums_overview.html
│   │   ├── album_detail.html
│   │   ├── album_edit.html
│   │   ├── album_add.html
│   │   ├── album_songs.html
│   │   ├── song_choices.html
│   │   └── account.html
│   ├── locale/                  # Translation files
│   ├── media/                   # Sample album covers
│   ├── migrations/              # Database migrations
│   └── management/
│       └── commands/
│           └── seed.py          # Data seeding command
│
├── app_pages/                   # Static pages app
│   ├── views.py                 # Views for home, about, contact, login
│   ├── forms.py                 # RecommendFriendForm
│   ├── urls.py                  # URL routing for static pages
│   ├── tests.py                 # Test suite for pages
│   ├── templates/
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   ├── login.html
│   │   └── recommend_friend.html
│   └── locale/                  # Page-specific translations
│
├── templates/                   # Shared templates
│   ├── base.html                # Base template with Bootstrap
│   ├── header.html              # Sidebar navigation
│   └── footer.html              # Footer component
│
├── static/
│   └── style.css                # Custom CSS with sidebar design
│
├── locale/                      # Project-wide translations
│   └── en/LC_MESSAGES/
│       └── django.po
│
├── sample_data/
│   └── sample_data.json         # Sample albums and songs
│
├── media/                       # User-uploaded album covers
│   └── album_covers/
│
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.8+
Django 4.2.6
pip (Python package installer)
```

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/BipinJungRai/MyMusicMaestro.git
cd MyMusicMaestro
```

2. **Create virtual environment** (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate   # On Windows
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Apply migrations**:
```bash
python manage.py migrate
```

5. **Seed database with sample data**:
```bash
python manage.py seed
```

6. **Run development server**:
```bash
python manage.py runserver
```

7. **Access the application**:
   - Open browser to `http://127.0.0.1:8000/`
   - Login with seeded user credentials (password: `password`)

---

## 🔬 Methodology

### 1. Database Design
- Designed normalized database schema with 4 models
- Implemented many-to-many relationships for flexibility
- Custom user model extending Django's AbstractUser
- Validation for business rules (positive prices, future dates)

### 2. Application Architecture
- **Two-app structure**: Separation of concerns
  - `app_pages`: Public/static pages
  - `app_album_viewer`: Album management functionality
- **MVC Pattern**: Models, Views, Templates clearly separated
- **URL Routing**: Organized by functionality
- **Template Inheritance**: Reusable base templates with Bootstrap

### 3. User Interface
- Bootstrap 5 for responsive design
- Custom sidebar navigation with JavaScript
- Form validation with Django Forms
- Image upload with preview
- Search functionality with query parameters

### 4. Testing
- Comprehensive test suite covering:
  - Model creation and validation
  - View functionality and responses
  - Authentication flow
  - Form handling
  - Error handling (404)
- Used Django's TestCase framework

### 5. Internationalization
- Django i18n framework implementation
- `.po` files for English translations
- Template tags for translatable strings
- Ready for multi-language expansion

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test app_album_viewer
python manage.py test app_pages

# Run with verbosity
python manage.py test --verbosity=2
```

### Test Coverage

- **Model Tests**: Album, Song, User, Comment creation and relationships
- **View Tests**: All views tested for correct responses and templates
- **Authentication Tests**: Login, logout, protected views
- **Form Tests**: Email recommendation form
- **Integration Tests**: CRUD operations end-to-end

---

## 📊 Key Results

### Technical Achievements

- ✅ **Full CRUD Implementation**: All database operations working correctly
- ✅ **User Authentication**: Secure login/logout with @login_required decorators
- ✅ **File Upload Handling**: Album covers with ImageField
- ✅ **Many-to-Many Management**: Complex song-album relationships
- ✅ **Email Integration**: Console email backend for recommendations
- ✅ **Search Functionality**: Case-insensitive title search
- ✅ **Data Seeding**: Automated database population
- ✅ **Form Validation**: Server-side validation with custom validators

### Grade Analysis (73%)

**Strengths**:
- Solid Django fundamentals and MVC architecture
- Comprehensive database design with proper relationships
- Good separation of concerns with two apps
- Extensive test coverage
- Internationalization implementation
- Clean code with comments

**Areas for Improvement**:
- Enhanced UI/UX design and polish
- More advanced features (ratings, favorites, playlists)
- Better error handling and user feedback
- API implementation for external access
- Advanced security features (CSRF, XSS protection)

---

## 🛠️ Technologies Used

- **Python 3.12**: Primary programming language
- **Django 4.2.6**: Web framework
- **SQLite**: Database (default Django db)
- **Bootstrap 5**: Frontend framework
- **Bootstrap Icons**: Icon library
- **Boxicons**: Additional icons
- **HTML5/CSS3**: Frontend markup and styling
- **JavaScript**: Interactive sidebar navigation

---

## 📚 Key Concepts Applied

### Django Framework
- Models (ORM)
- Views (Function-based)
- Templates (DTL)
- Forms
- URL Routing
- Authentication
- Admin Interface
- Migrations
- Management Commands

### Web Development
- HTTP Methods (GET, POST)
- CRUD Operations
- File Uploads
- Form Validation
- Session Management
- URL Parameters
- Redirects

### Database
- Relational Database Design
- Many-to-Many Relationships
- Foreign Keys
- Database Migrations
- ORM Queries
- Data Seeding

### Software Engineering
- MVC Architecture
- Separation of Concerns
- DRY Principle
- Testing (Unit, Integration)
- Version Control (Git)
- Documentation

---

## 🔍 Future Improvements

Potential enhancements for better functionality:

1. **User Features**:
   - User registration page
   - Password reset functionality
   - User profiles with avatars
   - Favorite albums feature
   - Album ratings and reviews

2. **Search & Discovery**:
   - Advanced search (by artist, format, price range)
   - Filtering and sorting options
   - Recently added albums
   - Popular albums ranking

3. **Social Features**:
   - Like/dislike comments
   - User-to-user messaging
   - Sharing to social media
   - Activity feed

4. **Technical Improvements**:
   - RESTful API (Django REST Framework)
   - Pagination for large datasets
   - AJAX for dynamic updates
   - Caching for performance
   - PostgreSQL for production
   - Docker containerization
   - CI/CD pipeline

5. **UI/UX**:
   - Modern responsive design
   - Dark mode toggle
   - Album artwork gallery view
   - Improved mobile experience
   - Loading states and animations

---

## 🎓 Learning Outcomes

This coursework demonstrated proficiency in:

1. **Web Application Development**: Full-stack development with Django
2. **Database Design**: Creating normalized schemas with relationships
3. **MVC Architecture**: Implementing model-view-controller pattern
4. **User Authentication**: Secure login systems with Django auth
5. **CRUD Operations**: Complete data management lifecycle
6. **Testing**: Writing comprehensive test suites
7. **Internationalization**: Multi-language application support
8. **Version Control**: Git workflow and repository management
9. **Documentation**: Clear code comments and README

---

## 👥 Author

- **Course**: COM1025 - Databases, Networks and the Web
- **Institution**: University of Surrey
- **Academic Year**: 2022-23
- **Grade**: 73%

---

## 📄 License

This project was submitted as coursework for COM1025 at the University of Surrey. All rights reserved.

---

## 🙏 Acknowledgments

- University of Surrey for providing the coursework framework
- Course instructors for guidance on web development best practices
- Django community for comprehensive documentation
- Openclipart for album cover icons
- Bootstrap team for the responsive framework

---

## 📞 Contact

For questions about this coursework project, please refer to the course module or contact through the University of Surrey student portal.

---

**Note**: This project was developed as part of academic coursework. The application is for educational purposes and demonstrates web development fundamentals with Django.
