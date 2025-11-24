<script>
  // URL вашего бэкенда. Если вы запускаете бэк локально, обычно это localhost:8000
  const API_URL = "http://localhost:8000"; 

  let login = '';
  let password = '';
  let isRegister = false; // Переключатель: вход или регистрация
  let errorMessage = '';

  function toggleMode() {
    isRegister = !isRegister;
    errorMessage = '';
  }

  async function handleAuth() {
    errorMessage = '';
    const endpoint = isRegister ? '/register' : '/login';
    
    try {
      const response = await fetch(`${API_URL}${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        // Отправляем JSON, как ожидает ваш Pydantic (schemas.UserLogin / UserCreate)
        body: JSON.stringify({ username: login, password: password }),
      });

      if (!response.ok) {
        const err = await response.json();
        throw new Error(err.detail || 'Ошибка сервера');
      }

      const data = await response.json();

      if (isRegister) {
        alert('Регистрация успешна! Теперь войдите.');
        toggleMode();
      } else {
        // Сохраняем токен (JWT)
        localStorage.setItem('access_token', data.access_token);
        alert(`Успешный вход! Токен: ${data.access_token.substring(0, 10)}...`);
        // Тут можно сделать редирект: window.location.href = '/dashboard';
      }
    } catch (e) {
      errorMessage = e.message;
      console.error(e);
    }
  }
</script>

<div class="authorization">
  <!-- Фон формы -->
  <div class="rectangle-2"></div>

  <!-- Кнопка действия -->
  <button class="button-primary-small-default" on:click={handleAuth}>
    <div class="div">
      {isRegister ? 'Зарегистрироваться' : 'Войти'}
    </div>
  </button>

  <!-- Кнопка ЭЦП (скрываем при регистрации для логики) -->
  {#if !isRegister}
  <button class="button-primary-small-default2">
    <div class="div2">Электронная подпись</div>
  </button>
  {/if}

  <!-- Поле Логин -->
  <div class="text-field-empty-placeholder">
    <div class="div3">Логин</div>
    <div class="frame-1">
      <input 
        class="div4 input-reset" 
        type="text" 
        placeholder="login" 
        bind:value={login} 
      />
    </div>
  </div>

  <!-- Поле Пароль -->
  <div class="text-field-empty-placeholder2">
    <div class="div3">Пароль</div>
    <div class="frame-1">
      <input 
        class="div4 input-reset" 
        type="password" 
        placeholder="**********" 
        bind:value={password} 
      />
    </div>
  </div>

  <!-- Ошибка -->
  {#if errorMessage}
    <div class="error-text">{errorMessage}</div>
  {/if}

  <!-- Заголовок -->
  <div class="div5">
    {isRegister ? 'Регистрация' : 'Войти'}
  </div>

  <!-- Ссылка на регистрацию/вход -->
  <div class="div6">
    <span>
      <span class="div-6-span">
        {isRegister ? 'Уже есть аккаунт? ' : 'Нет аккаунта? '}
      </span>
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <span class="div-6-span2" style="cursor: pointer;" on:click={toggleMode}>
        {isRegister ? 'Войти' : 'Зарегистрируйтесь'}
      </span>
    </span>
  </div>

  {#if !isRegister}
  <div class="div7" style="cursor: pointer;">Восстановить пароль</div>
  {/if}

  <!-- Иконка глаза. Убедитесь, что файл edit-hide0.svg лежит в папке public/ -->
  <img class="edit-hide" src="/edit-hide0.svg" alt="eye" />
</div>

<style>
  /* Дополнительный стиль для ошибки */
  .error-text {
    color: red;
    position: absolute;
    top: 260px;
    left: 568px;
    width: 320px;
    text-align: center;
    z-index: 5;
    font-size: 14px;
  }

  /* --- ВАШИ ОРИГИНАЛЬНЫЕ СТИЛИ --- */
  .input-reset {
    background: transparent;
    border: none;
    outline: none;
    width: 100%;
    height: 100%;
    padding: 0;
    margin: 0;
    font-family: inherit;
    font-size: inherit;
    color: inherit;
  }
  button {
    border: none;
    padding: 0;
    margin: 0;
    cursor: pointer;
  }
  .authorization,
  .authorization * {
    box-sizing: border-box;
  }
  .authorization {
    background: #f2f2f2;
    height: 1024px;
    position: relative;
    overflow: hidden;
    margin: 0 auto; 
  }
  .rectangle-2 {
    background: #ffffff;
    border-radius: 8px;
    width: 400px;
    height: 486px;
    position: absolute;
    left: 520px;
    top: 50%;
    translate: 0 -50%;
  }
  .button-primary-small-default {
    background: #cd1f15;
    border-radius: 4px;
    padding: 10px 17px 10px 17px;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    justify-content: center;
    width: 320px;
    position: absolute;
    left: 568px;
    top: 569px;
    z-index: 1; 
  }
  .div {
    color: #ffffff;
    text-align: center;
    font-family: "GolosText-Regular", sans-serif;
    font-size: 14px;
    line-height: 20px;
    font-weight: 400;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .button-primary-small-default2 {
    background: #f5f5f7;
    border-radius: 4px;
    padding: 10px 17px 10px 17px;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    justify-content: center;
    width: 320px;
    position: absolute;
    left: 568px;
    top: 625px;
    z-index: 1;
  }
  .div2 {
    color: #333333;
    text-align: center;
    font-family: "GolosText-Regular", sans-serif;
    font-size: 14px;
    line-height: 20px;
    font-weight: 400;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .text-field-empty-placeholder {
    padding: 8px 0px 16px 0px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
    justify-content: flex-start;
    width: 320px;
    position: absolute;
    left: calc(50% - 152px); 
    top: 345px;
    z-index: 1;
  }
  .div3 {
    color: #000000;
    text-align: left;
    font-family: "GolosText-Regular", sans-serif;
    font-size: 14px;
    line-height: 20px;
    font-weight: 400;
    position: relative;
  }
  .frame-1 {
    background: #ffffff;
    border-radius: 4px;
    border-style: solid;
    border-color: #a7a7ab;
    border-width: 1px;
    padding: 10px 14px 10px 14px;
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
    justify-content: flex-start;
    align-self: stretch;
    flex-shrink: 0;
    height: 34px;
    position: relative;
  }
  .div4 {
    color: #76767a;
    text-align: left;
    font-family: "GolosText-Regular", sans-serif;
    font-size: 14px;
    line-height: 20px;
    font-weight: 400;
    position: relative;
    display: flex; 
    align-items: center;
    justify-content: flex-start;
    width: 100%;
  }
  .text-field-empty-placeholder2 {
    padding: 8px 0px 16px 0px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
    justify-content: flex-start;
    width: 320px;
    position: absolute;
    left: calc(50% - 152px); 
    top: 431px;
    z-index: 1;
  }
  .div5 {
    color: #000000;
    text-align: left;
    font-family: "GolosText-SemiBold", sans-serif;
    font-size: 30px;
    line-height: 36px;
    font-weight: 600;
    position: absolute;
    left: 568px;
    top: 301px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    z-index: 1;
  }
  .div6 {
    text-align: center;
    font-family: "GolosText-Regular", sans-serif;
    font-size: 14px;
    line-height: 20px;
    font-weight: 400;
    position: absolute;
    left: 568px;
    bottom: 297px;
    width: 320px;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1;
  }
  .div-6-span {
    color: #333333;
  }
  .div-6-span2 {
    color: #0050b2;
  }
  .div7 {
    color: #0050b2;
    text-align: right;
    font-family: "GolosText-Regular", sans-serif;
    font-size: 14px;
    line-height: 20px;
    font-weight: 400;
    position: absolute;
    left: 740px;
    bottom: 487px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    z-index: 1;
  }
  .edit-hide {
    width: 16px;
    height: 16px;
    position: absolute;
    left: 858px;
    top: 476px;
    overflow: visible;
    aspect-ratio: 1;
    z-index: 2;
    cursor: pointer;
  }
</style>
