import axios from 'axios';


const AUTH_TOKEN = "test_token"; // Static authentication token
const API_URL = process.env.REACT_APP_API_URL || (window.location.hostname === "localhost" ? "http://localhost:8080" : "http://backend:8080");


// Create an Axios instance with default headers
const api = axios.create({
  baseURL: API_URL,
  headers: {
    "X-API-KEY": AUTH_TOKEN
  },
});

// ✅ Fetch all tasks
export const fetchTasks = async () => {
  try {
    const response = await api.get("/tasks/");
    return response.data || [];
  } catch (error) {
    console.error("Error fetching tasks:", error.response?.data || error.message);
    return [];
  }
};

// ✅ Fetch a single task by ID
export const fetchTaskById = async (taskId) => {
  try {
    const response = await api.get(`/tasks/${taskId}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching task ${taskId}:`, error.response?.data || error.message);
    return null;
  }
};

// ✅ Create a new task
export const createTask = async (task) => {
  try {
    const response = await api.post("/tasks/", task);
    return response.data;
  } catch (error) {
    console.error("Error creating task:", error.response?.data || error.message);
    return null;
  }
};

// ✅ Update an existing task
export const updateTask = async (taskId, updatedTask) => {
  try {
    const response = await api.put(`/tasks/${taskId}`, updatedTask);
    return response.data;
  } catch (error) {
    console.error(`Error updating task ${taskId}:`, error.response?.data || error.message);
    return null;
  }
};

// ✅ Delete a task
export const deleteTask = async (taskId) => {
  try {
    await api.delete(`/tasks/${taskId}`);
    return true;
  } catch (error) {
    console.error(`Error deleting task ${taskId}:`, error.response?.data || error.message);
    return false;
  }
};