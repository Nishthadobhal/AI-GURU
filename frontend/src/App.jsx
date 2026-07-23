import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Roadmap from "./pages/Roadmap";
import Mentor from "./pages/Mentor";
import Quiz from "./pages/Quiz";
import Revision from "./pages/Revision";
import Analytics from "./pages/Analytics";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
 <Route path="/roadmap" element={<Roadmap />} />

        <Route path="/mentor" element={<Mentor />} />

        <Route path="/quiz" element={<Quiz />} />

        <Route path="/revision" element={<Revision />} />

        <Route path="/analytics" element={<Analytics />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;