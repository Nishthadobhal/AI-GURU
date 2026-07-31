import { NavLink } from "react-router-dom";
import "./../styles/Sidebar.css";

function Sidebar() {
  return (
    <div className="sidebar">

      <h2 className="logo">AI Guru</h2>

      <NavLink to="/">Dashboard</NavLink>

      <NavLink to="/roadmap">Roadmap</NavLink>

      <NavLink to="/mentor">AI Mentor</NavLink>

      <NavLink to="/quiz">Quiz</NavLink>

      <NavLink to="/revision">Revision Plan</NavLink>

      <NavLink to="/analytics">Analytics</NavLink>

    </div>
  );
}

export default Sidebar;