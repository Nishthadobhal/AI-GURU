import { NavLink } from "react-router-dom";

function Sidebar() {

    const menu = [

        {
            name: "Roadmap",
            path: "/roadmap",
            icon: "🗺️"
        },

        {
            name: "Quiz",
            path: "/quiz",
            icon: "📝"
        },

        {
            name: "AI Mentor",
            path: "/mentor",
            icon: "🤖"
        },

        // {
        //     name: "Progress",
        //     path: "/progress",
        //     icon: "📈"
        // },

        // {
        //     name: "Profile",
        //     path: "/profile",
        //     icon: "👤"
        // }

    ];

    return (

        <div className="w-64 min-h-screen bg-[#161B22] text-white p-6">

            <h1 className="text-3xl font-bold mb-10">

                AI Guru

            </h1>

            <div className="space-y-3">

                {

                    menu.map((item) => (

                        <NavLink

                            key={item.name}

                            to={item.path}

                            className={({ isActive }) =>

                                `flex items-center gap-3 px-4 py-3 rounded-lg transition

                                ${

                                    isActive

                                    ?

                                    "bg-[#20E3B2] text-black"

                                    :

                                    "hover:bg-gray-800"

                                }`

                            }

                        >

                            <span>

                                {item.icon}

                            </span>

                            <span>

                                {item.name}

                            </span>

                        </NavLink>

                    ))

                }

            </div>

        </div>

    );

}

export default Sidebar;