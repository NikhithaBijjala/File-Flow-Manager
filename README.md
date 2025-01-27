
# File Management System with Client-Server Architecture

This project is a **file management system** that incorporates three core components: a **client**, a **server**, and a **cache**. The system is designed to optimize file retrieval and storage, ensuring efficient performance and seamless user experience.

---

## **Key Features**
1. **File Retrieval**:
   - The system first checks the **cache** for requested files.
   - If the file is not found in the cache, it retrieves the file from the **server**.

2. **File Upload**:
   - Files are uploaded directly to the **server**, bypassing the cache for efficiency.

3. **Optimized Performance**:
   - The use of a **cache** reduces latency and improves file retrieval speed for frequently accessed files.

4. **Scalable Architecture**:
   - The client-server architecture ensures the system can handle multiple clients and large files efficiently.

---

## **Core Components**
1. **Client**:
   - Handles user requests for file uploads and downloads.
   - Communicates with the cache and server.

2. **Server**:
   - Stores and manages files.
   - Responds to client requests for file retrieval.

3. **Cache**:
   - Temporarily stores frequently accessed files to reduce server load and improve retrieval speed.

---

## **How It Works**
1. **File Retrieval**:
   - The client requests a file.
   - The system first checks the cache.
     - If the file is found, it is returned to the client.
     - If not, the server retrieves the file and stores a copy in the cache for future requests.

2. **File Upload**:
   - The client uploads a file.
   - The file is stored directly on the server.

---

## **Technologies Used**
- **Python**: Core programming language.
- **Socket Programming**: For communication between the client and server.
- **Cache Implementation**: Using a local storage mechanism (e.g., dictionary or file-based cache).
- **File Handling**: For reading, writing, and managing files.

---

## **How to Run**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/file-management-system.git
   cd file-management-system
   ```

2. Start the server:
   ```bash
   python server.py
   ```

3. Start the client:
   ```bash
   python client.py
   ```

4. Follow the on-screen instructions to upload or retrieve files.

---
