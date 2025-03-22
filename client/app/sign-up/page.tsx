"use client"
import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import * as z from "zod"
import { Button } from "@/components/ui/button"
import { Form, FormControl, FormDescription, FormField, FormItem, FormLabel, FormMessage, } from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { PasswordInput } from "@/components/ui/password-input"
import { PhoneInput } from "@/components/ui/phone-input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { UtilityHandler } from "@/lib/form-handler"

export default function MyForm() {

    const formSchema = z.object({
        full_name: z.string().min(1).min(6).max(30),
        email: z.string(),
        password: z.string(),
        phone_number: z.string(),
        role: z.string()
    });

    const form = useForm<z.infer<typeof formSchema>>({
        resolver: zodResolver(formSchema),
    })

    return (
        <Form {...form}>
            <form onSubmit={form.handleSubmit((values) => UtilityHandler.onSubmitPost('/add_user', values))} className="space-y-8 max-w-3xl mx-auto py-20">

                <FormField
                    control={form.control}
                    name="full_name"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Enter your full name</FormLabel>
                            <FormControl>
                                <Input
                                    placeholder="shadcn"
                                    type="text"
                                    {...field} />
                            </FormControl>
                            <FormDescription>This is your public display name.</FormDescription>
                            <FormMessage />
                        </FormItem>
                    )}
                />

                <FormField
                    control={form.control}
                    name="email"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Email</FormLabel>
                            <FormControl>
                                <Input
                                    placeholder="shadcn"

                                    type="email"
                                    {...field} />
                            </FormControl>
                            <FormDescription>This is your public email</FormDescription>
                            <FormMessage />
                        </FormItem>
                    )}
                />

                <FormField
                    control={form.control}
                    name="password"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Password</FormLabel>
                            <FormControl>
                                <PasswordInput placeholder="Placeholder" {...field} />
                            </FormControl>
                            <FormDescription>Enter your password.</FormDescription>
                            <FormMessage />
                        </FormItem>
                    )}
                />


                <FormField
                    control={form.control}
                    name="password"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Password</FormLabel>
                            <FormControl>
                                <PasswordInput placeholder="Placeholder" {...field} />
                            </FormControl>
                            <FormDescription>Re-enter your password</FormDescription>
                            <FormMessage />
                        </FormItem>
                    )}
                />


                <FormField
                    control={form.control}
                    name="phone_number"
                    render={({ field }) => (
                        <FormItem className="flex flex-col items-start">
                            <FormLabel>Phone number</FormLabel>
                            <FormControl className="w-full">
                                <PhoneInput
                                    placeholder="Placeholder"
                                    {...field}
                                    defaultCountry="TR"
                                />
                            </FormControl>
                            <FormDescription>Enter your phone number.</FormDescription>
                            <FormMessage />
                        </FormItem>
                    )}
                />


                <FormField
                    control={form.control}
                    name="role"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Role</FormLabel>
                            <Select onValueChange={field.onChange} defaultValue={field.value}>
                                <FormControl>
                                    <SelectTrigger>
                                        <SelectValue placeholder="Select a verified email to display" />
                                    </SelectTrigger>
                                </FormControl>
                                <SelectContent className="bg-white text-black">
                                    <SelectItem value="Farmer">Farmer</SelectItem>
                                    <SelectItem value="Customer">Customer</SelectItem>
                                    <SelectItem value="Admin">Admin</SelectItem>
                                    <SelectItem value="Verifier">Verifier</SelectItem>
                                </SelectContent>
                            </Select>
                            <FormDescription>You can select your role here</FormDescription>
                            <FormMessage />
                        </FormItem>
                    )}
                />
                <Button type="submit">Submit</Button>
            </form>
        </Form>
    )
}