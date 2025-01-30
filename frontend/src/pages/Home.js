import React, { useState, useEffect } from "react";
import { fetchTasks, createTask, updateTask, deleteTask } from "../api";
import TaskList from "../components/TaskList";
import TaskForm from "../components/TaskForm";


const Home = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    const loadTasks = async () => {
      const data = await fetchTasks();
      setTasks(data);
    };
    loadTasks();
  }, []);

  // 📌 Add a new task
  const handleAddTask = async (task) => {
    const newTask = await createTask(task);
    if (newTask) {
      setTasks((prevTasks) => [...prevTasks, newTask]);
    }
  };

  // 📌 Update a task
  const handleUpdateTask = async (taskId, updatedTask) => {
    const updated = await updateTask(taskId, updatedTask);
    if (updated) {
      setTasks((prevTasks) =>
        prevTasks.map((task) => (task.id === taskId ? updated : task))
      );
    }
  };

  // 📌 Delete a task
  const handleDeleteTask = async (taskId) => {
    const success = await deleteTask(taskId);
    if (success) {
      setTasks((prevTasks) => prevTasks.filter((task) => task.id !== taskId));
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-white p-6 rounded-xl shadow-md w-full max-w-2xl">
        <h1 className="text-3xl font-bold text-center mb-4">Task Manager</h1>
        <TaskForm onSubmit={handleAddTask} />
        <TaskList tasks={tasks} onUpdate={handleUpdateTask} onDelete={handleDeleteTask} />
      </div>
    </div>
  );
};

export default Home;