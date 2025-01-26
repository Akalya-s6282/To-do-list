document.getElementById('addTaskBtn').addEventListener('click', () => {
      const taskInput = document.getElementById('taskInput');
        const taskList = document.getElementById('taskList');

          if (taskInput.value.trim()) {
              const li = document.createElement('li');
                  li.innerHTML = `
                        <span>${taskInput.value}</span>
                              <button class="delete-btn">Delete</button>
                                  `;
                                      
                                          // Mark task complete
                                              li.querySelector('span').addEventListener('click', () => {
                                                    li.querySelector('span').classList.toggle('completed');
                                                        });

                                                            // Delete task
                                                                li.querySelector('.delete-btn').addEventListener('click', () => {
                                                                      li.remove();
                                                                          });

                                                                              taskList.appendChild(li);
                                                                                  taskInput.value = '';
                                                                                    }
                                                                                    });
})