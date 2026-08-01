import { BrowserRouter, Routes, Route } from "react-router-dom";

import Landing from "../pages/Landing";
import Onboarding from "../pages/Onboarding";
import Roadmap from "../pages/Roadmap";

function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />} />
       <Route path="/onboarding" element={<Onboarding />} />
       <Route path="/roadmap" element={<Roadmap />} />
      </Routes>
    </BrowserRouter>
  );
}

export default AppRoutes;