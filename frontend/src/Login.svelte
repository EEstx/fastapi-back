<script>
  let isRegister = false;
  let username = "";
  let password = "";
  let errorMessage = "";

  const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

  async function handleSubmit() {
    const endpoint = isRegister ? "/auth/register" : "/auth/login";
    errorMessage = "";

    try {
      const response = await fetch(`${API_URL}${endpoint}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });

      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || "Ошибка запроса");
      }

      const data = await response.json();
      if (!isRegister) {
        localStorage.setItem("token", data.access_token);
        alert("Успешный вход!");
      } else {
        alert("Регистрация успешна! Теперь войдите.");
        isRegister = false;
      }
    } catch (err) {
      errorMessage = err.message;
    }
  }
</script>
<div class="login-page-wrapper">
  <div class="login-wrapper">
    <div class="card">
      <h2>{isRegister ? "Регистрация" : "Вход в систему"}</h2>
      
      <form on:submit|preventDefault={handleSubmit} class="form-group">
        <label>
          <span>Логин</span>
          <input type="text" bind:value={username} placeholder="Введите имя пользователя" required />
        </label>

        <label>
          <span>Пароль</span>
          <input type="password" bind:value={password} placeholder="Введите пароль" required />
        </label>

        {#if errorMessage}
          <div class="error">{errorMessage}</div>
        {/if}

        <button type="submit" class="primary-btn">
          {isRegister ? "Зарегистрироваться" : "Войти"}
        </button>

        {#if !isRegister}
          <button type="button" class="secondary-btn">Электронная подпись</button>
        {/if}
      </form>

      <div class="footer">
        {#if isRegister}
          <p>Уже есть аккаунт? <a href="#" on:click|preventDefault={() => (isRegister = false)}>Войти</a></p>
        {:else}
          <p>Нет аккаунта? <a href="#" on:click|preventDefault={() => (isRegister = true)}>Зарегистрируйтесь</a></p>
          <p><a href="#" class="forgot-password">Забыли пароль?</a></p>
        {/if}
      </div>
    </div>
  </div>
</div>
<style>
  .login-wrapper {
    width: 100%;
    max-width: 400px;
    padding: 20px;
  }

  .card {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(119, 61, 61, 0.08);
    text-align: center;
  }

  h2 {
    margin-bottom: 1.5rem;
    color: #333;
    font-size: 1.5rem;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  label {
    display: flex;
    flex-direction: column;
    text-align: left;
    gap: 0.4rem;
    font-size: 0.9rem;
    color: #555;
  }

  input {
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 1rem;
    transition: border-color 0.2s;
  }

  input:focus {
    outline: none;
    border-color: #646cff;
    box-shadow: 0 0 0 3px rgba(100, 108, 255, 0.1);
  }

  input::placeholder {
    color: #888; /* Был совсем светлый, теперь темно-серый */
    opacity: 1;  /* Обязательно для Firefox, чтобы цвет применился полностью */
  }
  input {
    padding: 0.75rem;
    border: 1px solid #ef7777ff;
    border-radius: 6px;
    font-size: 1rem;
    transition: border-color 0.2s;
    background-color: #fff; /* Убедись, что фон белый/светлый */
    color: #333; /* Цвет вводимого текста */
  }

  input::placeholder {
    color: #666; /* <-- ВОТ ТУТ регулируй яркость подсказки */
    opacity: 1;
  }

  input:focus {
    outline: none;
    border-color: #646cff;
    box-shadow: 0 0 0 3px rgba(100, 108, 255, 0.1);
  }

  button {
    padding: 0.75rem;
    border-radius: 6px;
    font-size: 1rem;
    cursor: pointer;
    border: none;
    transition: background 0.2s;
    font-weight: 600;
  }

  .primary-btn {
    background-color: #d32f2f; /* Твой красный цвет с картинки */
    color: white;
    margin-top: 0.5rem;
  }

  .primary-btn:hover {
    background-color: #b71c1c;
  }

  .secondary-btn {
    background-color: #f5f5f5;
    color: #333;
  }

  .secondary-btn:hover {
    background-color: #e0e0e0;
  }

  .error {
    color: #d32f2f;
    font-size: 0.9rem;
    background: #ffebee;
    padding: 0.5rem;
    border-radius: 4px;
  }

  .footer {
    margin-top: 1.5rem;
    font-size: 0.9rem;
    color: #666666ff;
  }

  a {
    color: #1976d2;
    text-decoration: none;
    font-weight: 500;
  }

  a:hover {
    text-decoration: underline;
  }

  .forgot-password {
    color: #888;
    font-size: 0.85rem;
  }
  :global(body) {
    /* Убираем отступы у body на случай, если они есть */
    margin: 0; 
}

/* Класс контейнера для центрирования */
.login-page-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh; /* Высота во весь экран */
    background-color: #f0f2f5; /* Цвет фона, если нужен */
    width: 100%;
}

</style>
