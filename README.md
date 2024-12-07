### **README: Yellow Pages Scraper**

---

### **Purpose**
This project is a **web scraping tool** designed to extract business information such as name, address, phone number, and services offered from [Yellow Pages Pakistan (ypages.pk)](https://ypages.pk). The tool is designed to allow users to input a service and location and scrape relevant data.  

**Disclaimer**: This project is created purely for **learning purposes** and as a **portfolio project**. It should not be used for commercial purposes or in ways that violate the website's terms of service.

---

### **Disclaimer**
1. **Educational Use Only**: The project is intended for personal learning and skill-building.
2. **Adhere to Website Policies**: Always ensure that scraping is permitted by the website's **Terms of Service**.
3. **Ethical Practices**: Avoid excessive server requests and implement delays as needed to prevent overloading the website.

---

### **How It Works**

1. **Inputs**:
   - The user is prompted to input:
     - **Service Type** (e.g., "Plumber")
     - **Location** (e.g., "Karachi")
   - These inputs are used to perform a search query on the Yellow Pages website.

2. **Automation**:
   - The script uses **Selenium** to automate browser tasks:
     - Opens the website.
     - Enters the user's search query into the search bar.
     - Initiates the search.

3. **Data Extraction**:
   - Extracts the following details for each listing on the search results page:
     - **Business Name**
     - **Address**
     - **Phone Number**
     - **Services Offered**
   - Data is appended to a list as dictionaries.

4. **Pagination**:
   - The script identifies the "Next Page" button and navigates through multiple pages, collecting data until the end of the results.

5. **Output**:
   - The collected data is stored in a **CSV file** (`output_data.csv`) for easy analysis.

6. **Error Handling**:
   - Handles cases where elements might be missing or inaccessible using exception handling.

---

### **Learning Objectives**
- Use **Selenium** for browser automation.
- Scrape structured data from dynamic websites.
- Handle common web scraping challenges like pagination and missing elements.

---
