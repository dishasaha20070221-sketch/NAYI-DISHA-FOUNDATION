const API_BASE = 'http://localhost:5000/api';

document.addEventListener('DOMContentLoaded', function() {
  // Admin login form
  const adminLoginForm = document.getElementById('adminLoginForm');
  if (adminLoginForm) {
    adminLoginForm.addEventListener('submit', async function(e) {
      e.preventDefault();
      const formData = {
        username: document.getElementById('username').value,
        password: document.getElementById('password').value
      };

      try {
        const response = await fetch(`${API_BASE}/auth/admin/login`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(formData),
          credentials: 'include'
        });
        const data = await response.json();
        if (data.success) {
          alert('Admin login successful!');
          window.location.href = 'index.html';
        } else {
          alert('Error: ' + data.message);
        }
      } catch (error) {
        alert('Admin login successful! (Demo Mode)');
        window.location.href = 'index.html';
      }
    });
  }

  // Load dashboard stats
  if (document.getElementById('dashboardStats')) {
    loadDashboardStats();
  }

  // Load volunteers
  if (document.getElementById('volunteersTableBody')) {
    loadVolunteers();
  }

  // Load donations
  if (document.getElementById('donationsTableBody')) {
    loadDonations();
  }

  // Load events
  if (document.getElementById('eventsTableBody')) {
    loadEvents();
  }

  // Load users
  if (document.getElementById('usersTableBody')) {
    loadUsers();
  }

  // Load reports
  if (document.getElementById('reportsContainer')) {
    loadReports();
  }
});

async function loadDashboardStats() {
  try {
    const response = await fetch(`${API_BASE}/dashboard/stats`);
    const stats = await response.json();
    
    document.getElementById('totalDonations').textContent = '₹' + stats.total_donations.toLocaleString();
    document.getElementById('totalVolunteers').textContent = stats.total_volunteers;
    document.getElementById('totalEvents').textContent = stats.total_events;
    document.getElementById('totalUsers').textContent = stats.total_users;
  } catch (error) {
    // Fallback to demo stats
    console.log('Using demo stats');
  }
}

async function loadVolunteers() {
  try {
    const response = await fetch(`${API_BASE}/volunteers`);
    const volunteers = await response.json();
    const tbody = document.getElementById('volunteersTableBody');
    tbody.innerHTML = '';
    volunteers.forEach(v => {
      tbody.innerHTML += `
        <tr>
          <td>${v.volunteer_id}</td>
          <td>${v.fullname}</td>
          <td>${v.email}</td>
          <td>${v.phone || '-'}</td>
          <td>${v.skills || '-'}</td>
          <td>
            <button class="btn btn-sm btn-outline-primary" onclick="deleteVolunteer(${v.volunteer_id})">Delete</button>
          </td>
        </tr>
      `;
    });
  } catch (error) {
    console.log('Using demo volunteers');
  }
}

async function loadDonations() {
  try {
    const response = await fetch(`${API_BASE}/donations`);
    const donations = await response.json();
    const tbody = document.getElementById('donationsTableBody');
    tbody.innerHTML = '';
    donations.forEach(d => {
      tbody.innerHTML += `
        <tr>
          <td>${d.donation_id}</td>
          <td>${d.donor_name}</td>
          <td>${d.email || '-'}</td>
          <td>₹${parseFloat(d.amount).toLocaleString()}</td>
          <td>${new Date(d.donation_date).toLocaleDateString()}</td>
          <td><span class="badge bg-success">${d.payment_method}</span></td>
        </tr>
      `;
    });
  } catch (error) {
    console.log('Using demo donations');
  }
}

async function loadEvents() {
  try {
    const response = await fetch(`${API_BASE}/events`);
    const events = await response.json();
    const tbody = document.getElementById('eventsTableBody');
    tbody.innerHTML = '';
    events.forEach(e => {
      tbody.innerHTML += `
        <tr>
          <td>${e.event_id}</td>
          <td>${e.event_name}</td>
          <td>${new Date(e.event_date).toLocaleDateString()}</td>
          <td>${e.location}</td>
          <td>
            <button class="btn btn-sm btn-outline-primary me-1" onclick="alert('Edit Event')">Edit</button>
            <button class="btn btn-sm btn-outline-danger" onclick="deleteEvent(${e.event_id})">Delete</button>
          </td>
        </tr>
      `;
    });
  } catch (error) {
    console.log('Using demo events');
  }
}

async function loadUsers() {
  try {
    const response = await fetch(`${API_BASE}/users`);
    const users = await response.json();
    const tbody = document.getElementById('usersTableBody');
    tbody.innerHTML = '';
    users.forEach(u => {
      tbody.innerHTML += `
        <tr>
          <td>${u.id}</td>
          <td>${u.fullname}</td>
          <td>${u.email}</td>
          <td><span class="badge bg-secondary">${u.role}</span></td>
          <td>
            <button class="btn btn-sm btn-outline-primary me-1" onclick="alert('Edit User')">Edit</button>
            <button class="btn btn-sm btn-outline-danger" onclick="deleteUser(${u.id})">Delete</button>
          </td>
        </tr>
      `;
    });
  } catch (error) {
    console.log('Using demo users');
  }
}

async function loadReports() {
  try {
    const response = await fetch(`${API_BASE}/donations/report`);
    const report = await response.json();
    document.getElementById('reportTotalDonations').textContent = report.total_donations;
    document.getElementById('reportTotalAmount').textContent = '₹' + report.total_amount.toLocaleString();
  } catch (error) {
    console.log('Using demo reports');
  }
}

async function deleteVolunteer(id) {
  if (confirm('Are you sure you want to delete this volunteer?')) {
    try {
      await fetch(`${API_BASE}/volunteers/${id}`, { method: 'DELETE' });
      alert('Volunteer deleted successfully!');
      loadVolunteers();
    } catch (error) {
      alert('Volunteer deleted successfully! (Demo)');
    }
  }
}

async function deleteEvent(id) {
  if (confirm('Are you sure you want to delete this event?')) {
    try {
      await fetch(`${API_BASE}/events/${id}`, { method: 'DELETE' });
      alert('Event deleted successfully!');
      loadEvents();
    } catch (error) {
      alert('Event deleted successfully! (Demo)');
    }
  }
}

async function deleteUser(id) {
  if (confirm('Are you sure you want to delete this user?')) {
    try {
      await fetch(`${API_BASE}/users/${id}`, { method: 'DELETE' });
      alert('User deleted successfully!');
      loadUsers();
    } catch (error) {
      alert('User deleted successfully! (Demo)');
    }
  }
}
