import reflex as rx


class State(rx.State):
    resources_unlocked: bool = False
    report_text: str = ""

    def unlock_resources(self):
        self.resources_unlocked = True

    def generate_report(self):
        self.report_text = "This is a sample AI-generated report for your project."


# ---------- HOME ----------
def index():
    return rx.center(
        rx.vstack(
            rx.heading("Student Hub 🚀", size="9"),
            rx.text("Projects | Reports | Notes"),

            rx.link(
                rx.button("View Pricing", color_scheme="blue"),
                href="/pricing"
            ),

            spacing="4"
        ),
        height="100vh"
    )


# ---------- PRICING ----------
def pricing():
    return rx.center(
        rx.vstack(
            rx.heading("Pricing"),

            rx.box(
                rx.text("📚 Resources (₹1)"),
                rx.button(
                    "Unlock",
                    on_click=State.unlock_resources,
                    color_scheme="green"
                ),
                rx.cond(
                    State.resources_unlocked,
                    rx.text("✅ Resources Unlocked")
                ),
                padding="1em",
                border="1px solid gray"
            ),

            rx.box(
                rx.text("🧾 Report Generator (₹5)"),
                rx.button(
                    "Generate",
                    on_click=State.generate_report,
                    color_scheme="blue"
                ),
                rx.text(State.report_text),
                padding="1em",
                border="1px solid gray"
            ),

            rx.box(
                rx.text("💻 Projects (₹49)"),
                rx.link(
                    rx.button("View Projects"),
                    href="/projects"
                ),
                padding="1em",
                border="1px solid gray"
            ),

            spacing="4"
        ),
        height="100vh"
    )


# ---------- PROJECTS ----------
def projects():
    return rx.center(
        rx.vstack(
            rx.heading("Projects"),

            rx.box(
                rx.text("AI Chat App"),
                rx.text("After payment, send screenshot on Telegram"),
                padding="1em",
                border="1px solid gray"
            ),

            rx.box(
                rx.text("Portfolio Website"),
                rx.text("After payment, send screenshot on Telegram"),
                padding="1em",
                border="1px solid gray"
            ),

            spacing="4"
        ),
        height="100vh"
    )


# ---------- APP ----------
app = rx.App()
app.add_page(index)
app.add_page(pricing, route="/pricing")
app.add_page(projects, route="/projects")