const API_BASE = 'http://localhost:5000/api';

document.addEventListener('DOMContentLoaded', function() {
  // Volunteer form
  const volunteerForm = document.getElementById('volunteerForm');
  if (volunteerForm) {
    volunteerForm.addEventListener('submit', async function(e) {
      e.preventDefault();
      const formData = {
        fullname: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        skills: document.getElementById('interest').value,
        availability: 'Flexible'
      };

      try {
        const response = await fetch(`${API_BASE}/volunteers`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(formData)
        });
        const data = await response.json();
        if (data.success) {
          alert('Thank you for registering as a volunteer! We will contact you soon.');
          volunteerForm.reset();
        } else {
          alert('Error: ' + data.message);
        }
      } catch (error) {
        alert('Thank you for registering as a volunteer! (Demo Mode)');
        volunteerForm.reset();
      }
    });
  }

  // Donation form
  const donateForm = document.getElementById('donateForm');
  if (donateForm) {
    donateForm.addEventListener('submit', async function(e) {
      e.preventDefault();
      
      let amount = 0;
      const selectedAmount = document.querySelector('input[name="amount"]:checked');
      if (selectedAmount) {
        amount = parseFloat(selectedAmount.value);
      } else {
        const customAmount = document.getElementById('customAmount');
        if (customAmount) amount = parseFloat(customAmount.value);
      }

      const formData = {
        donor_name: document.getElementById('donorName').value,
        email: document.getElementById('donorEmail').value,
        amount: amount,
        payment_method: 'upi'
      };

      try {
        const response = await fetch(`${API_BASE}/donations`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(formData)
        });
        const data = await response.json();
        if (data.success) {
          alert('Thank you for your donation! Your contribution will help us make a difference.');
          donateForm.reset();
        } else {
          alert('Error: ' + data.message);
        }
      } catch (error) {
        alert('Thank you for your donation! (Demo Mode)');
        donateForm.reset();
      }
    });
  }

  // Contact form
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      alert('Thank you for your message! We will get back to you soon.');
      contactForm.reset();
    });
  }

  // Login form
  const loginForm = document.getElementById('loginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', function(e) {
      e.preventDefault();
      alert('Login successful! Redirecting to home page...');
      loginForm.reset();
      window.location.href = 'index.html';
    });
  }

  // Load events on events page
  const eventsContainer = document.getElementById('eventsContainer');
  if (eventsContainer) {
    loadEvents();
  }
});

async function loadEvents() {
  try {
    const response = await fetch(`${API_BASE}/events`);
    const events = await response.json();
    const container = document.getElementById('eventsContainer');
    container.innerHTML = '';
    events.forEach(event => {
      const eventCard = `
        <div class="col-md-6 mb-4">
          <div class="card shadow-sm">
            <div class="card-body">
              <h5 class="fw-bold text-primary">${event.event_name}</h5>
              <p><i class="bi bi-calendar-event"></i> ${new Date(event.event_date).toLocaleDateString()}</p>
              <p><i class="bi bi-geo-alt"></i> ${event.location}</p>
              <p>${event.description}</p>
            </div>
          </div>
        </div>
      `;
      container.innerHTML += eventCard;
    });
  } catch (error) {
    console.log('Using demo events');
  }
}
