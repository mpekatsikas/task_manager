import React from 'react';

const TaskList = ({ tasks, onUpdate, onDelete }) => {
  console.log("Rendering tasks:", tasks); // Debug log

  if (tasks.length === 0) {
    return <p>No tasks available. Try adding one!</p>;
  }

  return (
    <ul>
      {tasks.map((task) => (
        <li key={task.id}>
          <span>{task.title} - {task.completed ? "✅ Completed" : "❌ Pending"}</span>
          <button onClick={() => onUpdate(task.id, { ...task, completed: !task.completed })}>
            {task.completed ? "Mark as Incomplete" : "Mark as Complete"}
          </button>
          <button onClick={() => onDelete(task.id)}>🗑 Delete</button>
        </li>
      ))}
    </ul>
  );
};

export default TaskList;