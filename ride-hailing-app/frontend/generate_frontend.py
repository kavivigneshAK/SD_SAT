import os
import subprocess

frontend_files = {
    "src/App.jsx": """import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import DriverDashboard from './pages/DriverDashboard';
import CustomerDashboard from './pages/CustomerDashboard';
import AdminDashboard from './pages/AdminDashboard';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/driver" element={<DriverDashboard />} />
        <Route path="/customer" element={<CustomerDashboard />} />
        <Route path="/admin" element={<AdminDashboard />} />
      </Routes>
    </Router>
  );
}
export default App;
""",
    "src/pages/Home.jsx": """import React from 'react';
import { Link } from 'react-router-dom';
export default function Home() {
    return (
        <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
            <h1 className="text-4xl font-bold mb-8 text-blue-600">Ride Hailing App</h1>
            <div className="space-x-4">
                <Link to="/login" className="px-4 py-2 bg-blue-500 text-white rounded">Login</Link>
                <Link to="/register" className="px-4 py-2 bg-green-500 text-white rounded">Register</Link>
            </div>
        </div>
    );
}""",
    "src/pages/Login.jsx": """import React from 'react';
export default function Login() {
    return (
        <div className="min-h-screen bg-gray-100 flex items-center justify-center">
            <div className="bg-white p-8 rounded shadow-md w-96">
                <h2 className="text-2xl font-bold mb-4">Login</h2>
                <input type="email" placeholder="Email" className="w-full mb-4 p-2 border rounded" />
                <input type="password" placeholder="Password" className="w-full mb-4 p-2 border rounded" />
                <button className="w-full bg-blue-500 text-white p-2 rounded">Login</button>
            </div>
        </div>
    );
}""",
    "src/pages/Register.jsx": """import React from 'react';
export default function Register() {
    return (
        <div className="min-h-screen bg-gray-100 flex items-center justify-center">
            <div className="bg-white p-8 rounded shadow-md w-96">
                <h2 className="text-2xl font-bold mb-4">Register</h2>
                <input type="text" placeholder="Name" className="w-full mb-4 p-2 border rounded" />
                <input type="email" placeholder="Email" className="w-full mb-4 p-2 border rounded" />
                <input type="password" placeholder="Password" className="w-full mb-4 p-2 border rounded" />
                <select className="w-full mb-4 p-2 border rounded">
                    <option value="CUSTOMER">Customer</option>
                    <option value="DRIVER">Driver</option>
                </select>
                <button className="w-full bg-green-500 text-white p-2 rounded">Register</button>
            </div>
        </div>
    );
}""",
    "src/pages/CustomerDashboard.jsx": """import React from 'react';
export default function CustomerDashboard() { return <div className="p-8"><h1 className="text-3xl">Customer Dashboard</h1><div id="map" className="h-64 bg-gray-200 mt-4 flex items-center justify-center">Map Placeholder</div></div>; }""",
    "src/pages/DriverDashboard.jsx": """import React from 'react';
export default function DriverDashboard() { return <div className="p-8"><h1 className="text-3xl">Driver Dashboard</h1></div>; }""",
    "src/pages/AdminDashboard.jsx": """import React from 'react';
export default function AdminDashboard() { return <div className="p-8"><h1 className="text-3xl">Admin Dashboard</h1></div>; }"""
}

# Assume vite project is already created.
for path, content in frontend_files.items():
    full_path = os.path.join("/Users/kavivignesh/Documents/SD SAT/ride-hailing-app/frontend", path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

print("Generated frontend files.")
