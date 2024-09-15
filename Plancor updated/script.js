// Translation object containing translations for each language
const translations = {
    en: {
        title: "Welcome to My Website",
        description: "This is a demonstration of manually switching content between English and Hindi."
    },
    hi: {
        title: "मेरी वेबसाइट पर आपका स्वागत है",
        description: "यह अंग्रेजी और हिंदी के बीच सामग्री को मैन्युअल रूप से स्विच करने का प्रदर्शन है।"
    }
};

// Function to translate the page content
function translatePage() {
    const language = document.getElementById("languageSwitcher").value;
    document.querySelectorAll("[data-key]").forEach(function(element) {
        const key = element.getAttribute("data-key");
        element.textContent = translations[language][key];
    });
}
