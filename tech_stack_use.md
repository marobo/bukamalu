## **Tech Stack & How Each Tool Is Used**

### **1\. Django (Backend – Brain of the System)**

**Role:**

* Generate unique share links

* Store temporary location sessions

* Connect host and visitor together

* Control privacy & expiration

**What Django handles:**

* Create a **share session ID** (e.g. `/share/abc123`)

* Store:

  * Host latitude & longitude

  * Visitor latitude & longitude (when allowed)

* Auto-expire sessions (e.g. after 1–2 hours)

* Serve HTML pages

**Models (simple example):**

`LocationSession`  
`- id`  
`- session_code`  
`- host_lat`  
`- host_lng`  
`- visitor_lat`  
`- visitor_lng`  
`- is_active`  
`- created_at`

---

### **2\. Leaflet.js (Map Display – Visual Part)**

**Role:**

* Show map

* Show markers for both people

* Draw line between host and visitor

**Leaflet features used:**

* OpenStreetMap tiles (free)

* Blue marker → Host

* Green marker → Visitor

* Dashed line → distance between them

**Why Leaflet is good:**  
 ✔ Lightweight  
 ✔ Works well on slow internet  
 ✔ No Google Maps API key needed

---

### **3\. HTML (Structure – Simple Screens)**

**Used for:**

* Share button page

* Visitor map page

* Permission messages

**Key screens:**

1. **Home screen**

   * Big button: `SHARE MY LOCATION`

2. **Visitor screen**

   * Map

   * “Allow location” message

   * Stop sharing button

---

### **4\. CSS (Design – Simple & Friendly)**

**Design rules:**

* Big buttons

* Large text

* High contrast colors

* Mobile-first layout

**Focus:**

* Elder-friendly

* Local language ready

* No clutter

---

### **5\. Vanilla JavaScript (Logic – No Framework)**

**Role:**

* Get GPS location from phone

* Send location to Django

* Update map live

* Handle permissions

**Browser API used:**

`navigator.geolocation.watchPosition()`

**What JS does:**

* Detect location

* Send updates every few seconds

* Update Leaflet markers

* Stop sharing when user exits

---

## **How the System Works (Step-by-Step)**

### **STEP 1: Host Shares Location**

1. User opens `/`

2. Clicks **Share My Location**

3. JS gets GPS location

4. Django creates session

Django returns share link:

 `https://yourapp.com/share/abc123`

5.   
6. User sends link via WhatsApp

---

### **STEP 2: Visitor Opens Link**

1. Visitor clicks the link

2. Page asks:  
    **“Allow location to help guide you”**

3. Visitor taps **Allow**

4. Visitor’s location sent to Django

---

### **STEP 3: Two-Way Live Map**

* Leaflet shows:

  * 📍 Host location

  * 🚶 Visitor location

* JS updates both locations every few seconds

* Line shows distance between them

---

### **STEP 4: Stop Sharing**

* Visitor or Host clicks **STOP**

* Django marks session inactive

* Location updates stop

* Data deleted later automatically

---

## **Minimal Folder Structure (Simple)**

`project/`  
`├── app/`  
`│   ├── models.py`  
`│   ├── views.py`  
`│   ├── urls.py`  
`│`  
`├── templates/`  
`│   ├── home.html`  
`│   ├── share.html`  
`│`  
`├── static/`  
`│   ├── css/style.css`  
`│   ├── js/location.js`  
`│`  
`└── manage.py`

---

## **Privacy & Safety (Important to Mention)**

* Location shared only with permission

* No login required

* Data auto-deletes

* Sharing stops anytime

---

## **Why This Stack Is Perfect for Your Country**

✔ Works on low-end phones  
 ✔ Low data usage  
 ✔ No Google dependency  
 ✔ Easy to maintain  
 ✔ Can be hosted cheaply

