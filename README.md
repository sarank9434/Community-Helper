# 🧑‍🤝‍🧑 Community Help Provider
**KMC Hackathon 1.0 Project Report**

## 👥 Team: Tech Innovators
* **Lead Developer:** [Your Name]
* **Mentor:** Santosh Sharma

---

## 📄 Abstract
Social media is effective for entertaining content and informal communications but it is not a good platform for requesting or offering simple helps. In times of local emergencies or daily community needs, information is often scattered across social media or lost in group chats. **Community Help Provider** is a centralized web platform that connects people who *need* help with those who can *offer* it. By using real-time location tagging and categorized posting, the system ensures that help reaches the right person in the right location at the right time.

## ❓ Problem Statement
When a crisis occurs (like a medical emergency) or when a citizen wants to volunteer, there is no dedicated platform to match needs with resources locally. 
* **Fragmentation:** Needs are posted across various apps (Facebook, WhatsApp).
* **Searchability:** No way to filter requests by "Urgency" or "Category."
* **Location:** Difficult to pinpoint exactly where help is required in a city like Kathmandu.

## 🏗️ Existing System
Our system allows user for create posts that are classified as request post or offer post. Users can quickly get the email or the phone number of the post creator. We have implemented authentication in our platform. Each user has his/her user profile which consists of information such as email, contact, first name, last name, location, etc. The user can only create a post if he or she is logged in. the home page is scrollable and contains diffent cards and each card is for a diffrent post. The feed or the home page displays all the posts sorted by its creation date. The user can log in or sign up to a new account. A user can also delete his or her own post.

## 💡 Proposed Solution
Our system automates the community aid workflow:
1. **Creation:** Users post "Need" or "Offer" with descriptions.
2. **Categorization:** Needs are sorted into Medical, Education, Food, etc.
3. **Geolocation:** Precise coordinates via `PlainLocationField`.
4. **Automation:** Django Signals automatically manage user profiles. Contact, Location and User's name is automatically taken from user's profile insted of asking in each post creation.
5. **Efficiency:** A live feed that automatically hides "Closed" posts.

## 🎯 Objectives
* **Efficiency:** Drastically reduce the time taken to find local help.
* **Accuracy:** Use specific status codes (Open, In-Progress, Closed) to track aid.
* **Digitalization:** Maintain organized, cloud-based community records.
* **Accessibility:** A clean, Bootstrap-based UI accessible on any device.

## 🛠️ Technology Used
| Layer | Technology |
| :--- | :--- |
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap 5 |
| **Backend** | Python 3.13, Django 6.0.1 |
| **Database** | SQLite3 (Relational) |
| **Maps** | Leaflet / OpenStreetMap via `django-location-field` |
| **Architecture** | MVT (Model-View-Template) |

## 📐 System Wireframe & Workflow
* **Home Feed:** Chronological list of active help requests.
* **Profile System:** Automatically generated via Django `post_save` signals.
* **Workflow:** [User Auth] → [Post Creation] → [Location Tagging] → [Resolution] → [Status Update].



## 📈 Results
Based on our development and testing:
* **Response Speed:** Needs are visible to the entire community instantly upon posting.
* **Organization:** Data is categorized by priority and city automatically.
* **Reliability:** The `.exclude(status=Closed)` logic ensures users only see relevant, active posts.

## ✅ Advantages
* **Precision:** Real-time map integration for exact location finding.
* **Scalability:** The category system allows for endless types of community aid.
* **Accountability:** Every post is linked to a verified user profile.
* **Eco-Friendly:** Replaces manual bulletin boards and paper tracking.

## ⚠️ Limitations
* Requires a stable internet connection for map services.
* Assumes users have basic digital literacy to update post statuses.

## 🚀 Future Improvements
* **Real-time Notifications:** SMS alerts to nearby volunteers when an "Emergency" post is created.
* **Mobile App:** Dedicated progressive web apps (PWA) for better field usage. 
* **Offline Mode:** Local syncing for areas with poor connectivity.
* **Moderator Users:** Allows moderators, government departments or organizatios to observe real time posts.

## 🏁 Conclusion
The Community Help Provider bridges the gap between traditional mutual aid and modern technology. By digitizing the act of helping, we allow citizens to focus more on the support itself and less on the search for where to provide it.
