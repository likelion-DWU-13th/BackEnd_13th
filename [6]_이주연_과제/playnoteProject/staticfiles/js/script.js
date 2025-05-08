function confirmDelete() {
  return confirm("정말 삭제하시겠습니까?");
}

function showLoginAlert() {
  const modal = document.getElementById('loginAlert');
  if (modal) {
    modal.style.display = 'flex';
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const createBtn = document.querySelector('.cute-fab.yellow-btn');
  const modal     = document.getElementById('loginAlert');
  const closeBtn  = document.getElementById('loginAlertClose');

  if (modal && closeBtn) {
    // 모달 닫기 버튼 클릭 시
    closeBtn.addEventListener('click', () => {
      modal.style.display = 'none';
    });

    // 모달 외부 클릭 시 닫기
    window.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.style.display = 'none';
      }
    });
  }

  // "+" 버튼 클릭 시
  if (createBtn && modal) {
    createBtn.addEventListener('click', (e) => {
      if (createBtn.classList.contains('disabled')) {
        e.preventDefault();
        modal.style.display = 'flex';
      }
    });
  }
});
