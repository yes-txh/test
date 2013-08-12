################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../shell/yes_2/execute.c \
../shell/yes_2/main.c \
../shell/yes_2/parser.c \
../shell/yes_2/prompt.c \
../shell/yes_2/readline.c \
../shell/yes_2/redirect.c 

OBJS += \
./shell/yes_2/execute.o \
./shell/yes_2/main.o \
./shell/yes_2/parser.o \
./shell/yes_2/prompt.o \
./shell/yes_2/readline.o \
./shell/yes_2/redirect.o 

C_DEPS += \
./shell/yes_2/execute.d \
./shell/yes_2/main.d \
./shell/yes_2/parser.d \
./shell/yes_2/prompt.d \
./shell/yes_2/readline.d \
./shell/yes_2/redirect.d 


# Each subdirectory must supply rules for building sources it contributes
shell/yes_2/%.o: ../shell/yes_2/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cross GCC Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


